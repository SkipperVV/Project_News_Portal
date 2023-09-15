from django import template
from django_filters import FilterSet

register = template.Library()
from ..models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'author': ['exact'],
            'title': ['exact'],
            'post_time': ['gt'],
        }

