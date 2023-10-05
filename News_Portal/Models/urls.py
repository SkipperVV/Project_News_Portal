from django.urls import path

from .views import PostView, PostsListAll, PostCreateView, PostDeleteView, PostUpdateView
from .views_old import PostsList, PostDetail
from .view_categories import Categories_list_View, subscribe

from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', PostsListAll.as_view()),
    path('one_by_one/', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='posts'),
    path('search/', PostView.as_view()),
    path('create/', PostCreateView.as_view(), name='create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),

    path('admin/', admin.site.urls),
    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),

    path('categories/<int:pk>', Categories_list_View.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]
