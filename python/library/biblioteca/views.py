from django.shortcuts import render, redirect
from django.db.models import Sum
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class HomeView(TemplateView):
    template_name = "biblioteca/home.html"
