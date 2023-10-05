from typing import Any
from django.shortcuts import get_object_or_404, render, reverse, redirect
from django.views import View
from django.core.mail import send_mail
from datetime import datetime

from .models import Category, Post
from .views import PostsListAll
from django.contrib.auth.decorators import login_required

class Categories_list_View(PostsListAll):
    model = Post
    template_name = 'categories_list.HTML'
    context_object_name='categories_posts_list'

    def get_queryset(self):
        self.category= get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by ('-post_time')
        return queryset

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['is_subscriber'] = self.request.user in self.category.subscribers.all()
        context['category']=self.category
        return context

@login_required
def subscribe(request, pk):    
    user=request.user
    category=Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = f'Вы успешно подписались на рассылку по категории "{category}"'
    return render(request, 'suscribe.html',{'category' : category, 'message' : message})



