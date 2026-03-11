from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cards/', views.user, name='user'),
    path('add/', views.add_user, name='add')
]