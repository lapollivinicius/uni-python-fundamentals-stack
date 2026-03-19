from django.urls import path
from .views import Posts, addPost, postPage, newPost, deletePost
from .comment import add_comment, delete_comment

urlpatterns = [
    path('', Posts, name='posts'),
    path('add/', addPost, name='add_post'),
    path('<int:post_id>/', postPage, name='post_page'),
    path('addcomment/', add_comment, name='add_comment'),
    path('newpost/', newPost, name='new_post'),
    path('deletecomment/<int:comment_id>', delete_comment, name='deletecomment'),
    path('deletepost/<int:post_id>', deletePost, name='deletepost')

]

