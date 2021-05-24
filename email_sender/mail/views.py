from django.shortcuts import render
from .models import Sender
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
