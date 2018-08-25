from django.conf.urls import url
from .views import FeedBackView


app_name = 'feedback'

urlpatterns = [
    url('post_feedback/', FeedBackView.as_view(), name='post_feedback'),
]
