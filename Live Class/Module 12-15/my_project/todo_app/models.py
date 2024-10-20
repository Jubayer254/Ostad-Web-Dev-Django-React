from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title # <- When prints obj return this


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField()
    
    def __str__(self):
        return self.first_name + ' ' +self.last_name # <- When prints obj return this


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateField(null=True, blank=True)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books") # 1 TO MANY
    author = models.ManyToManyField(Author, related_name="books") # MANY TO MANY
    
    def __str__(self):
        return self.first_name + ' ' +self.last_name # <- When prints obj return this
