from datetime import datetime
from typing import Any

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
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


class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('Models.add_post', 
                           'Models.change_post')
    template_name = 'create.html'
    form_class = PostForm


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('Models.change_post',)
    # login_url = '/login/'
    template_name = 'create.html'
    form_class = PostForm


    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('Models.delete_post')    
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
