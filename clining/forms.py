from django import forms
from .models import *



from django import forms
from .models import *



class OrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderForm
        fields = ['name', 'email', 'phone_number', 'category']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': "text",
                'placeholder': "Имя",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': "email",
                'placeholder': "Почта",
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'type': "text",
                'name': "phone",
                'placeholder': "Номер телефона",
            }),
            'category': forms.Select(attrs={
                "class": "custom-select custom-select-lg mb-3"
            })

        }

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'phone_number', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'type': 'text'
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone',
                'type': 'text'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Loyiha haqida bizga xabar bering',
                'type': 'text'
            })
        }


# class AllForm(forms.ModelForm):
#     class Meta:
#         model = Orders
#         exclude = ('roomname', 'roomname', 'roomprice' )
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Name',
#                 'type': 'text'
#             }),
#             'phone_number': forms.NumberInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Phone',
#                 'type': 'text'
#             }),
#             }