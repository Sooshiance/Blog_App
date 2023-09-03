from django.shortcuts import render

from .models import Post, Comment, Like, Complaicent


def allPost(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})
