
# Create your views here.
from django.http import HttpResponse
from django.http import HttpRequest
from django.template import loader
from .forms import RoutineForms
from django.shortcuts import render, redirect

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def user(request):
    return HttpResponse('CARDS')

def add_user(request):
    if request.method == "POST":
        form = RoutineForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {
        'form':RoutineForms
    }
    return render(request, 'add_user.html', context)



