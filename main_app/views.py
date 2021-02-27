from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def posts_index(request):
    return render(request, 'posts/index.html', { 'posts': posts })