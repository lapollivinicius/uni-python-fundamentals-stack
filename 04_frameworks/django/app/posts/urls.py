from django.urls import path
from .views import Posts, addPost, postPage

urlpatterns = [
    path('', Posts, name='posts'),
    path('add/', addPost, name='add_post'),
    path('<int:post_id>/', postPage, name='post_page')
]
