from django.contrib import admin
from .views import home
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('users/', include('users.urls')),
    path('', home, name='home')
]
