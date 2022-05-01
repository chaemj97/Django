from django.db import models

# Create your models here.

class BlogPosting(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self) -> str:
        return f'{self.pk}: {self.title}'