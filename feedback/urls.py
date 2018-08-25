from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import post_feedback
from django.views.generic import TemplateView

app_name = 'feedback'
urlpatterns = [
    path('post_feedback/', post_feedback, name='post_feedback'),
]