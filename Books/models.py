from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year = models.IntegerField()
    category = models.CharField(max_length=100)
    pages = models.IntegerField(default=0)  # Add a default value here

    def __str__(self):
        return self.title