from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
from .templatetags.filter import PostFilter

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

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

# class PostDetail(ListView):
#     model = Post
#     template_name = 'post.html'
#     context_object_name = 'posts_count'

#     def get_context_data(self, form):
#         # context = super().get_context_data(**kwargs)
#         form.instance.author=self.request.user.author
#         how_many = len(Post.objects.filter(author=self.author, post_time=datetime.date.today()))
#         today = datetime.date.today()
#         return super().form_valid(form)




