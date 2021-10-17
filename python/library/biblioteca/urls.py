from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),
    path('books/', views.BookView.as_view(), name="books"),
    path('books/new/', views.CreateBookView.as_view(), name="new_book"),
    path('books/<pk>/update', views.UpdateBookView.as_view(), name="update_book"),
    path('books/<pk>/delete', views.DeleteBookView.as_view(),name="delete_book"),
    path('clients/', views.ClientView.as_view(), name="clients"),
    path('clients/new/', views.CreateClientView.as_view(), name="new_client"),
    path('clients/<pk>/update', views.UpdateClientView.as_view(), name="update_client"),
    path('clients/<pk>/delete', views.DeleteClientView.as_view(),name="delete_client")
]