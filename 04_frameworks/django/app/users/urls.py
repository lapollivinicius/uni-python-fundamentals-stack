from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.auth_login, name='login'),
    path('register/', views.auth_register, name='register'),
]
