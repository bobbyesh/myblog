from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
