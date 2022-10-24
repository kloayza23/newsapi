from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Article(models.Model):
    author=models.CharField(max_length=50)
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=200)
    body=models.TextField()
    location=models.CharField(max_length=120)
    publication_date=models.DateField()
    active=models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f"{self.author}{self.title}"
