from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q 

from .models import Post, Comment, Like, Complaint
from .forms import UserPost, UserComment, UserLike, UserComplante


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
            if form.is_valid():
                title = form.cleaned_data['title']
                txt = form.cleaned_data['txt']
                is_private = form.cleaned_data['is_private']
                p = Post.objects.create(title=title,txt=txt,is_private=is_private,user=request.user)
                p.save()
                messages.success(request, '')
                return redirect('')
            else:
                messages.error(request, f"{form.errors}")
                return redirect('')
        else:
            form = UserPost()
        return render(request, 'blog/sendpost.html', {'form':form})
    else:
        messages.info(request, '')
        return redirect('LOGIN')


def sendComment(request, title):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserComment(request.POST)
            post = Post.objects.get(title=title)
            if form.is_valid():
                txt = form.cleaned_data['txt']
                c = Comment.objects.create(txt=txt,comment=post,user=request.user)
        else:
            form = UserComment()
        return render(request, 'blog/sendcomment.html', {'form':form})
    else:
        messages.info(request, '')
        return redirect('LOGIN')


def sendLike(request, title):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserLike(request.POST)
        else:
            form = UserLike()
        return render(request, 'blog/sendlike.html', {'form':form})
    else:
        messages.info(request, '')
        return redirect('LOGIN')


def sendComplante(request, comment):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserComplante(request.POST)
        else:
            form = UserComplante()
        return render(request, 'blog/sendcomplante.html', {'form':form})
    else:
        messages.info(request, '')
        return redirect('LOGIN')
