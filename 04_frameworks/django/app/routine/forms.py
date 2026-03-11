from django import forms  
from .models import Routine

class RoutineForms(forms.ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'email']
    