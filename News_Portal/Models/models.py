from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        posts_rating = 0
        comments_rating = 0
        post_comments_rating = 0

        posts = Post.objects.filter(author=self)
        for i in posts:
            posts_rating += i.rating
        comments = Comment.objects.filter(user=self.user)
        for j in comments:
            comments_rating += j.rating
        post_comments = Comment.objects.filter(post__author=self)
        for k in post_comments:
            post_comments_rating += k.rating

        print('posts_rating= ', posts_rating)
        print('comments_rating=', comments_rating)
        print('post_comments_rating=', post_comments_rating)

        self.rating = posts_rating * 3 + comments_rating + post_comments_rating
        self.save()

    def __str__(self):
        return (f"Author's name is: %s" % self.user)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    article = 'AR'
    news = 'NW'

    POSITION = [(article, 'Статья'), (news, 'Новость'), ]

    post_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    post_type = models.CharField(max_length=10, choices=POSITION, default=news)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        small_text = self.text[0:124] + '...'
        return small_text

class PostCategory(models.Model):  # OneToMany
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


