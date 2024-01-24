from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
from Models import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewset)
router.register(r'comments', views.CommentViewset)
router.register(r'authors', views.AuthorViewest)

urlpatterns = [
    # path('pages/', include('django.contrib.flatpages.urls')),
    path('i18n/', include('django.conf.urls.i18n')), # подключаем перевод
    path('admin/', admin.site.urls),
    path('news/', include('Models.urls')),
    path('serializers/', include(router.urls)),
    # path('create/', include('Models.urls')),

    # path('login/', admin.site.urls, name='login'),
    # path('create/admin/login/',admin.site.urls),
    # path('accounts/login/',admin.site.urls),

    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
