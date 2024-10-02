from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
class Upload(models.Model):
    name = models.CharField(max_length=150)
    descp = models.TextField()
    image = models.ImageField(upload_to="reciepe")
    video=models.FileField(upload_to="video")
