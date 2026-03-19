from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from . import models


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

@login_required(login_url='/users/login/')
def deletePost(request, post_id):

    post = get_object_or_404(models.Post, id=post_id)

    if post.created_by != request.user:
        return HttpResponseForbidden("it doesn't yours")
    else:
        post.delete()

    return redirect('posts')

def postPage(request, post_id):
    post = models.Post.objects.get(id=post_id)
    comments = models.Comment.objects.filter(post=post).order_by('created_at')
    return render(request, 'post_page.html', {'post': post, 'comments': comments})

