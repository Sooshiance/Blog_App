from django.shortcuts import render

from .models import Post, Comment, Like, Complaicent


def allPost(request):
    posts = Post.objects.all().filter(is_private=False)
    return render(request, 'index.html', {'posts':posts})


def seinglePost(request, title):
    post = Post.objects.get(title=title)
    comments = Comment.objects.all().filter(post=title).filter(admin_approval=True)
    return render(request, 'post.html', {})
