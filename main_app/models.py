from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    date = models.DateField('date created')
    
    def __str__(self):
        return self.title