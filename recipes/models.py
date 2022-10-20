from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name
