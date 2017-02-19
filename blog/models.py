from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(unique=True, populate_from='title')

    def __str__(self):
        return self.title
