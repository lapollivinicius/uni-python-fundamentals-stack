from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True, null=False)
    name = models.CharField(max_length=60, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=60, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username