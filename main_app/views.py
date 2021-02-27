from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Post
# Create your views here.


def home(request):
    return render(request, 'home.html')

def posts_index(request):
    return render(request, 'posts/index.html', { 'posts': posts })

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body', 'date']