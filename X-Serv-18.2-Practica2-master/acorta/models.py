from django.db import models

# Create your models here.

class Pages(models.Model):
    url = models.CharField(max_length=32)
    page = models.IntegerField()
