from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


@login_required
def posts_index(request):
    posts = Post.objects.filter(user=request.user)
    # favorites = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


@login_required
def favorite_page(request):
    # if post.is_favorite == True:
    posts = Post.objects.all()
    return render(request, 'posts/favorite.html', {'posts': posts})


@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comment_form = CommentForm()

    return render(request, 'posts/detail.html', {
        'post': post, 'comment_form': comment_form
    })


def add_comment(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.post_id = post_id
        new_comment.save()
    return redirect('posts_detail', post_id=post_id)


def favorite_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.is_favorite:
        post.is_favorite = False
    else:
        post.is_favorite = True
    post.save()
    return redirect('posts_detail', post_id=post_id)


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body', 'date']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body']


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'


class CommentUpdate(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body']


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = '/'
