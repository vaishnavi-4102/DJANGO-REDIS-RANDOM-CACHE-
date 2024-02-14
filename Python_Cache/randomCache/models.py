from django.db import models

# Create your models here.

class Cache_Data(models.Model):
    key = models.CharField(max_length=40)
    value = models.TextField()