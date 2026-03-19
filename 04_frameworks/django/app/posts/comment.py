from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

@login_required(login_url='/users/login/')
def add_comment(request):

    body = request.POST.get('comment')
    post_id = request.POST.get('post_id')
    user = request.user

    if not body or not body.strip():
        messages.error(request, "Adicione um comentário válido")
        return redirect('post_page', post_id=post_id)

    models.Comment.objects.create(
        body=body,
        post_id=post_id,
        created_by=user
    )

    return redirect('post_page', post_id=post_id)

@login_required(login_url='/users/login/')
def delete_comment(request, comment_id):

    comment = get_object_or_404(models.Comment, id=comment_id)

    if comment.created_by != request.user:
        return HttpResponseForbidden("it doesn't yours")
    else:
        comment.delete()

    return redirect('post_page', post_id=comment.post.id)
