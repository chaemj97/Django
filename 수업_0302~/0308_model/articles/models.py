from turtle import title, update
from django.db import models

# Create your models here.
class Article(models.Model):
    # 필드 정의
    # 길이 짧은건 CharField, 긴건 TextField
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
