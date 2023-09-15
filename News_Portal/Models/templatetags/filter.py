from django import template
from django_filters import FilterSet

register = template.Library()
from ..models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'author': ['exact'],
            'title': ['icontains'],
            'post_time': ['gt'],
        }
        #Выбор даты из календаря
# class PostFilter(FilterSet):
#     post_time = DateFilter(field_name='post_time', widget=forms.DateInput(attrs={'type': 'date'}),
#                            lookup_expr='date__gt')
#
#     class Meta:
#         model = Post
#         fields = {
#             'author': ['exact'],
#             'title': ['exact'],
#         }

