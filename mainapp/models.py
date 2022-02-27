from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Mainhome(models.Model):
    search_text = models.CharField(max_length=200, null=True)

