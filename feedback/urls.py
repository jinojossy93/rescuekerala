from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(), name='fb')
]