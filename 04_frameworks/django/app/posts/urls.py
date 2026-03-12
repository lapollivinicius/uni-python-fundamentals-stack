from django.urls import path
from .views import Posts, addPost

urlpatterns = [
    path('', Posts),
    path('add/', addPost),
]
