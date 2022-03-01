from django.contrib.auth.models import User
from django.db import models
from django import forms


class Post(models.Model):

    recipe_type = models.CharField(max_length=200, null=True)
    recipe_material = models.CharField(max_length=200, null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='post/d', null=False)
    ""
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

