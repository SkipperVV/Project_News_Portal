from django.urls import path

from .views import PostView, PostsListAll, PostCreateView, PostDeleteView, PostUpdateView
from .views_old import PostsList, PostDetail
from .view_categories import Categories_list_View, subscribe, unsubscribe

from django.contrib import admin
from django.urls import path
from django.urls import include
# cashe
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(PostsListAll.as_view())),#кэширование на главную страницу (одну минуту)
    path('one_by_one/', cache_page(300)(PostsList.as_view())),#Добавьте кэширование на страницы с новостями (по 5 минут на каждую)
    path('<int:pk>', PostDetail.as_view(), name='posts'),
    path('search/', PostView.as_view()),
    path('create/', PostCreateView.as_view(), name='create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),

    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),

    path('categories/<int:pk>', Categories_list_View.as_view(), name='categories_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
]
