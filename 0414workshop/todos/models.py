from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    do = models.CharField(max_length=200)
    finish = models.BooleanField(default=False)
