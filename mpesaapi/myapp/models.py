
from django.db import models
# from .models import Item

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


