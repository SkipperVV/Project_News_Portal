from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, Max
from django.db.models.functions import Coalesce  # Меняет None to 'пользовательское значение'

article = 'AR'
news = 'NW'
POSITION = [(article, 'Статья'), (news, 'Новость'), ]


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = self.post_set.aggregate(posts_rat=Coalesce(Sum('rating'), 0)).get(
            'posts_rat')  # или через get или получить значение по ключу ['posts_rat']
        comments_rating = self.user.comment_set.aggregate(posts_rat=Coalesce(Sum('rating'), 0))[
            'posts_rat']
        post_comments_rating = self.post_set.aggregate(post_comments_rat=Coalesce(Sum('comment__rating'), 0))[
            'post_comments_rat']
        #           или так:
        # posts_rating = Post.objects.filter(author=self).aggregate(posts_rat=Coalesce(Sum('rating'), 0))[
        #     'posts_rat']  # ['posts_rat'] обращение по ключу
        # comments_rating = Comment.objects.filter(user=self.user).aggregate(comments_rat=Coalesce(Sum('rating'), 0))[
        #     'comments_rat']
        # post_comments_rating = \
        # Comment.objects.filter(post__author=self).aggregate(post_comments_rat=Coalesce(Sum('rating'), 0))[
        #     'post_comments_rat']

        print('Raiting of author: ', self.user)
        print('posts rating= ', posts_rating)
        print('comments rating=', comments_rating)
        print('post comments rating=', post_comments_rating)

        self.rating = posts_rating * 3 + comments_rating + post_comments_rating
        self.save()

    @staticmethod
    def get_best_author():  # Вывести username и рейтинг лучшего пользователя
        max_rating = Author.objects.aggregate(Max("rating"))["rating__max"]
        best_author = Author.objects.get(rating=max_rating).user
        print(f'Наибольший рейтинг {max_rating} имеет автор {best_author}')

    # def __str__(self):
    # return ("автор: %s" % self.user)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    post_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=101)
    text = models.TextField()
    post_type = models.CharField(max_length=2, choices=POSITION, default=article)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    @staticmethod
    def get_best_post():  # Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи
        max_post_rating = Post.objects.aggregate(Max("rating"))["rating__max"]
        post = Post.objects.get(rating=max_post_rating)
        post_time = post.post_time.strftime('%d.%m.%Y')
        post_type = post.post_type
        author = post.author.user
        title = post.title

        print(f"Лучшей статьёй, по мнению наших многочисленных подписчиков, является {post_type} '{title}'.\n"
              f"{post_type} была опубликована {post_time} и уже получила {max_post_rating} миллионов положительных отзывов."
              f"\nАвтор {post_type} - товарищ {author}\n"
              f"Краткое изложение {post_type}:")
        post.preview()

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        small_text = self.text[0:124] + '...'
        return small_text


class Comment(models.Model):
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):  # OneToMany
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
