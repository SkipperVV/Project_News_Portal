from django.views.generic import ListView

from .models import Post
from .templatetags.filters import PostFilter


class PostView(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'post'
    ordering = '-post_time'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
