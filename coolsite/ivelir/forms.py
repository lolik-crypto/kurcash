from django import forms
from django.contrib.auth.models import User

class PurchaseForm(forms.Form):
    name = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='Email')
