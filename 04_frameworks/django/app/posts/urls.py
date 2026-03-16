from django.urls import path
from .views import Posts, addPost, postPage
from .comment import add_comment

urlpatterns = [
    path('', Posts, name='posts'),
    path('add/', addPost, name='add_post'),
    path('<int:post_id>/', postPage, name='post_page'),
    path('add_comment', add_comment, name='add_comment')
]

