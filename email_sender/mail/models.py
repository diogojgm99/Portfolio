from django.db import models

# Create your models here.
class Sender(models.Model):
    senderName = models.CharField(max_length=50)
    texto = models.CharField(max_length=500)