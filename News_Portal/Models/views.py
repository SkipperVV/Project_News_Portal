import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .forms import PostForm
from .models import Post
from .templatetags.filter import PostFilter
from .tasks import info_after_new_post

import logging
logging.debug('Debug')
logging.info('Info')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')

class PostsListAll(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.utcnow()
        context['posts_quantity'] = len(Post.objects.all())
        return context


class PostView(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    ordering = '-post_time'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.datetime.utcnow()
        return context
    

class PostCreateView(PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'create.html'
    permission_required = ('Models.add_post',
                           'Models.change_post')
    context_object_name = 'posts_today'

    def form_valid(self, form):
        post = form.save(commit=False)
        form.instance.author = self.request.user.author
        today = datetime.date.today()
        limit = today - datetime.timedelta(days=1)
        # Check if posts > 3 per day
        if len(Post.objects.filter(author=post.author, post_time__gte=limit)) >= 3:
            # then refuse to post
            return render(self.request, 'refused_to_post.html')
        post.save()
        #Реализовать рассылку уведомлений подписчикам после создания новости
        info_after_new_post.delay(form.instance.pk)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.datetime.utcnow()
        # context['how_many'] = Post.objects.filter()
        return context


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('Models.change_post',)
    template_name = 'create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, 
    # который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ('Models.delete_post')
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
