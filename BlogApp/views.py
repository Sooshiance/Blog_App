from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q 

from .models import Post, Comment, Like, Complaicent
from .forms import UserPost


def allPost(request):
    posts = Post.objects.all().filter(is_private=False)
    return render(request, 'blog/index.html', {'posts':posts})


def singlePost(request, title):
    post = Post.objects.get(title=title)
    comments = Comment.objects.all().filter(post=title).filter(admin_approval=True)
    return render(request, 'blog/post.html', {'post':post, 'comments':comments})


def sendPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserPost(request.POST)
        else:
            form = UserPost()
        return render(request, 'blog/sendpost.html', {'form':form})
    else:
        messages.info(request, '')
        return redirect('LOGIN')
