from django.urls import path

from .views import *


urlpatterns = [
    path('', allPost, name='POSTS'),
    path('<str:title>/', seinglePost, name='POST'),
]
