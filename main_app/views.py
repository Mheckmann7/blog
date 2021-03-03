from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
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
    return render(request, 'posts/index.html', {'posts': posts})


@login_required
def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    # post_form = PostForm()s
    # 'post_form': post_form
    return render(request, 'posts/detail.html', {'post': post})


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
    success_url = '/posts/'
