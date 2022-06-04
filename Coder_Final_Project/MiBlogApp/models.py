from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatars', blank=True, null=True)

    def __str__(self):
        return self.user.username

class Pages(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=100)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title+' - '+self.author
