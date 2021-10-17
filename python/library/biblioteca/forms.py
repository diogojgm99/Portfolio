from django import forms
from django.forms import fields
from .models import Book, Client, Reservation

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"