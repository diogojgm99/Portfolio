from django import forms
from django.forms.forms import Form
from django.forms import Textarea

class UserForm(forms.Form):
    email = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'cols': 100, 'rows': 20}))


