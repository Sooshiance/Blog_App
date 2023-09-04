from django.urls import path

from .views import *


urlpatterns = [
    path('', allPost, name='POSTS'),
    path('<str:title>/', singlePost, name='POST'),
    path('post/', sendPost, name='POST'),
    path('<str:title>/comment/', sendComment, name='COMMENT'),
    path('<str:title>/like/', sendLike, name='LIKE'),
]
