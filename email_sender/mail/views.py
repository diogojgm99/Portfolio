from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from .forms import UserForm


# Create your views here.
def home(request):
    #admin_mail=settings.EMAIL_HOST
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail(subject,message,sender,['user@email.com'])
        return render(request,'home.html',{'form':form})
    
    form = UserForm
    return render(request,'home.html',{'form':form})
