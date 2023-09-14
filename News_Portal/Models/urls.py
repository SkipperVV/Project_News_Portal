from django.urls import path

from .views import PostView
from .views_old import PostsList, PostDetail

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostView.as_view())
]
