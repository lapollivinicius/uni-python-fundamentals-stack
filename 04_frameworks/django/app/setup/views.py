
# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render, redirect

def home(request):
    name = 'Jorge'
    return render('request', 'index.html', {'name': name})