'''Импортируем класс, который говорит нам о том,
что в этом представлении мы будем выводить список объектов из БД'''
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

# from pprint import pprint
class PostsList(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        context['posts_quantity'] = len(Post.objects.all())# или в html {{posts|length}}
        # pprint(context)
        return context

    '''В этот раз мы будем использовать DetailView. Он отличается от ListView тем, что возвращает конкретный объект, 
    а не список всех объектов из БД. Адрес, однако, будет немного отличаться. В него надо будет добавить идентификатор 
    товара, который мы хотим получить.
    Для этого снова перейдём в файл Models/views.py и добавим в него представление PostDetail, 
    которое будет выдавать информацию об одной статье.'''

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'



