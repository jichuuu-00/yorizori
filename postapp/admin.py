from django.contrib import admin

# Register your models here.

from postapp.models import Post
admin.site.register(Post)