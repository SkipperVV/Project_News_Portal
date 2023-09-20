from datetime import datetime
from typing import Any

from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import PostForm
from .models import Post
from .templatetags.filter import PostFilter


class PostsListAll(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    # def sort_choice(self, item_to_sort):
    #     self.ordering = str(item_to_sort)
    #     return self.ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['posts_quantity'] = len(Post.objects.all())
        return context


class PostView(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = '-post_time'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.utcnow()
        return context


class PostCreateView(CreateView):
    template_name = 'create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления
class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
