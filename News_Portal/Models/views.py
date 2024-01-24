import datetime
from django.utils import timezone
from django.shortcuts import redirect
import pytz #  импортируем стандартный модуль для работы с часовыми поясами

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, View

from .forms import PostForm
from .models import Post
from .templatetags.filter import PostFilter
from .tasks import info_after_new_post

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions

from Models.serializers import *
from Models.models import *

from django.utils.translation import gettext as _ # импортируем функцию для перевода
 
class PostsListAll(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now()
        context['posts_quantity'] = len(Post.objects.all())
        context['timezones'] = pytz.common_timezones #  добавляем в контекст все доступные часовые пояса
        context['current_time'] = timezone.now()
        return context
    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/news')

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

# добавим сериализаторы
class PostViewset(viewsets.ModelViewSet):
   queryset = Post.objects.all()
   serializer_class = PostSerializer
   # def list(self, request, format=None):
   #     return Response([])


class CommentViewset(viewsets.ModelViewSet):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer


class AuthorViewest(viewsets.ModelViewSet):
   queryset = Author.objects.all()
   serializer_class = AuthorSerializer