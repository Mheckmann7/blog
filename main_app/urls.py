from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_index, name='posts_index'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
]
