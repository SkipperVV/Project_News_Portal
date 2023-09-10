'''Импортируем класс, который говорит нам о том,
что в этом представлении мы будем выводить список объектов из БД'''
from django.views.generic import ListView, DetailView
from .models import Post

class PostsList(ListView):
    model = Post
    ordering = 'post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'

    '''В этот раз мы будем использовать DetailView. Он отличается от ListView тем, что возвращает конкретный объект, 
    а не список всех объектов из БД. Адрес, однако, будет немного отличаться. В него надо будет добавить идентификатор 
    товара, который мы хотим получить.
    Для этого снова перейдём в файл simpleapp/views.py и добавим в него представление ProductDetail, 
    которое будет выдавать информацию об одном товаре.'''

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'
