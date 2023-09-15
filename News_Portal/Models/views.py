from datetime import datetime
from typing import Any
from django.shortcuts import render
from django.views.generic import ListView

from .models import Post
from .templatetags.filter import PostFilter


class PostView(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'Post'
    ordering = '-post_time'
    paginate_by = 1

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.utcnow()
        return context
