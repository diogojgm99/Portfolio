from django.db import models
from django.db.models.deletion import CASCADE
import datetime

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=30)
    unit_price = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return "/ingredients/"

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return "/menu_item"
    
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient =models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)

    def get_absolute_url(self):
        return "/menu_item"

    def enough(self):
        return self.quantity <= self.ingredient.quantity

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.date.today)

    def get_absolute_url(self):
        return "/purchases"