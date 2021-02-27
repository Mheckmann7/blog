from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def posts_index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    # post_form = PostForm()s
    # 'post_form': post_form
    return render(request, 'posts/detail.html', {'post': post})


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body', 'date']
    success_url = '/posts/'


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'body']


class PostDelete(DeleteView):
    model = Post
    success_url = '/posts/'
