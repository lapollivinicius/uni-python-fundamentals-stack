from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required

def Posts(request):
    posts = models.Post.objects.all().order_by('-created_at')
    return render(request, 'posts.html', {'posts': posts})

@login_required(login_url='/users/login/')
def addPost(request):
    return render(request, 'add_posts.html')

@login_required(login_url='/users/login/')
def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')

        if title and body:
            models.Post.objects.create(
                title=title,
                body=body,
                created_by=request.user
            )

    return redirect('posts')

def postPage(request, post_id):
    post = models.Post.objects.get(id=post_id)
    comments = models.Comment.objects.filter(post=post).order_by('created_at')
    return render(request, 'post_page.html', {'post': post, 'comments': comments})