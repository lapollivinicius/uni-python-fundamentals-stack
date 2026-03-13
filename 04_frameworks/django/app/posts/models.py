from django.db import models
from users.models import User

class Post(models.Model):
    title = models.CharField(max_length=60, null=False)
    subject = models.CharField(max_length=60, null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.created_by} on {self.post}'
