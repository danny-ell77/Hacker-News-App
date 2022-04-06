from django.urls import path

from base.api.resources import *

urlpatterns = [
    path('stories', StoryList.as_view()),
    path('story/<str:pk>', StoryDetail.as_view()),
]
