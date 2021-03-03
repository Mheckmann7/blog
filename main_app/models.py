from django.db import models
from django.urls import reverse
# Create your models here.
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    date = models.DateField('date created')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'post_id': self.id})
