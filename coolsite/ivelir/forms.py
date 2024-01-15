from django import forms
from django.contrib.auth.models import User

class PurchaseForm(forms.Form):
    name = forms.CharField(label='Отзыв')
    email = forms.EmailField(label='Email')
