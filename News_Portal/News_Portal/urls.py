
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # path('pages/', include('django.contrib.flatpages.urls')),
    path('i18n/', include('django.conf.urls.i18n')), # подключаем перевод
    path('admin/', admin.site.urls),
    path('news/', include('Models.urls')),
    # path('create/', include('Models.urls')),

    # path('login/', admin.site.urls, name='login'),
    # path('create/admin/login/',admin.site.urls),
    # path('accounts/login/',admin.site.urls),

    path('', include('protect.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
]
