from django.db import models
from django.db.models.deletion import CASCADE
import datetime

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)

    def get_absolute_url(self):
        return "/books/"

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return "/clients/"

class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    begin_date = models.DateTimeField(default=datetime.date.today)
    end_date = models.DateTimeField()
    deliver_date = models.DateTimeField()
    fine = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return "/reservation/"
