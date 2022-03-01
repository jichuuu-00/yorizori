from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='post/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

