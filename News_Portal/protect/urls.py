from django.urls import path
from .views import IndexView
from django.views.generic import TemplateView

urlpatterns = [
    path('', IndexView.as_view()),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]