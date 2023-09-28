
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('pages/', include('django.contrib.flatpages.urls')),
    # path('admin/', admin.site.urls),
    # path('login/', admin.site.urls),
    path('news/', include('Models.urls')),
    path('', include('Models.urls')),

    # path('login/', admin.site.urls, name='login'),
    # path('create/admin/login/',admin.site.urls),
    # path('accounts/login/',admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),

]
