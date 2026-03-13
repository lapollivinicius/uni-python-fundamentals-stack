from posts.models import Post, User, Comment

user = User.objects.get(id=1)
post = Post.objects.get(id=2)

comment = Comment.objects.create(
    post=post,
    created_by=user,
    body="This is another comment"
)

comment.save()