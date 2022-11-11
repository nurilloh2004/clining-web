from django import forms
from .models import *

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Double
        fields = ('name', 'price')
