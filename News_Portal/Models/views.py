from datetime import datetime
from typing import Any
from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import Post
from .templatetags.filter import PostFilter

class PostsListAll(ListView):
    model = Post
    ordering = '-post_time'
    template_name = 'posts.html'
    context_object_name = 'posts'

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
