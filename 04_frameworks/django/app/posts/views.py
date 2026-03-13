from django.shortcuts import render
from . import models

def Posts(request):
    posts = models.Post.objects.all().order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})

def addPost(request):
    return render('request', 'add_posts.html')

def postPage(request, post_id):
    post = models.Post.objects.get(id=post_id)
    comments = models.Comment.objects.filter(post=post).order_by('created_at')
    return render(request, 'post_page.html', {'post': post, 'comments': comments})