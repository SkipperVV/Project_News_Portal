from django.urls import path

from .views import PostView, PostsListAll
from .views_old import PostsList, PostDetail

urlpatterns = [
    path('', PostsListAll.as_view()),
    path('one_by_one/', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostView.as_view()),
]
