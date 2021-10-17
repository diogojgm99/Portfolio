from django.shortcuts import render, redirect
from django.db.models import Sum
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Client, Reservation
from .forms import BookForm, ClientForm, ReservationForm

# Create your views here.
class HomeView(TemplateView):
    template_name = "biblioteca/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["books"] = Book.objects.all()
        context["clients"] = Client.objects.all()
        context["reservations"] = Reservation.objects.all()
        return context

##############################################
###########      Book Views            #######
##############################################

class BookView(ListView):
    model = Book
    template_name = "biblioteca/book.html"

class CreateBookView(CreateView):
    model= Book
    template_name = "biblioteca/new_book.html"
    form_class = BookForm

class UpdateBookView(UpdateView):
    model = Book
    template_name = "biblioteca/update_book.html"
    form_class = BookForm

class DeleteBookView(DeleteView):
    model = Book
    template_name = "biblioteca/delete_book.html"
    success_url = "/books/"

##############################################
###########      Client Views          #######
##############################################

class ClientView(ListView):
    model = Client
    template_name = "biblioteca/client.html"

class CreateClientView(CreateView):
    model= Client
    template_name = "biblioteca/new_client.html"
    form_class = ClientForm

class UpdateClientView(UpdateView):
    model = Client
    template_name = "biblioteca/update_client.html"
    form_class = ClientForm

class DeleteClientView(DeleteView):
    model = Client
    template_name = "biblioteca/delete_client.html"
    success_url = "/clients/"