from tkinter import CASCADE
from django.db import models

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=100)
    issue_a = models.CharField(max_length=100)
    issue_b = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    vote = models.ForeignKey(Vote,on_delete=models.CASCADE)
    pick = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content