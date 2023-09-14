from django_filters import FilterSet
from django import template
register = template.Library()
from ..models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            # 'author': ['icontains'],
            # 'title': ['icontains'],
            # 'post_time': ['gt'],
        }
