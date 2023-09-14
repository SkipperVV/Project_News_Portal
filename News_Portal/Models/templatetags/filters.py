from django_filters import FilterSet

from ..models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            # 'author': ['icontains'],
            # 'title': ['icontains'],
            'post_type': ['gt'],
        }
