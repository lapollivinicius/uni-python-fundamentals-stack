from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from django.contrib.auth import login

class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "username"
        self.fields["password1"].label = "password"
        self.fields["password2"].label = "password (again)"

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

def auth_register(request):
    
    if request.method == 'POST':
      form = MyUserCreationForm(request.POST)
      if form.is_valid():
        login(request, form.save())
        return redirect('posts')
      
    else: 
        form = MyUserCreationForm()

    return render(request, 'register.html', {'form': form})

def auth_login(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('posts')
        
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

#@mariejulie123