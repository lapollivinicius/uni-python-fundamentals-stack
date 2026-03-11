from django.db import models

# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)