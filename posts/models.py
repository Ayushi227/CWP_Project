from django.db import models

# Create your models here.
class Post(models.Model):
    word = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.word}"