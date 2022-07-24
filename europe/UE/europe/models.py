from django.db import models
import  europe.settings as s
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5, default="")
    currency = models.CharField(max_length=50,default="Euro")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Country"

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    group = models.CharField(max_length = 255, choices = s.TAG_GROUPS, default = "Menu")

    def __str__(self):
        return self.name

class Report(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    display = models.BooleanField(default=True)
    submenu = models.ForeignKey(Tag, related_name='tag_submenu', limit_choices_to={'group': 'Submenu'}, on_delete= models.CASCADE)
    menu = models.ForeignKey(Tag, related_name='tag_menu', limit_choices_to={'group': 'Menu'}, on_delete= models.CASCADE)
    title = models.CharField(max_length=255, default="")
    
    def __str__(self):
        return self.name

class Data_report(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE, related_name='country_data')
    year = models.IntegerField(default=2000)
    report = models.ForeignKey(Report, related_name='report', on_delete=models.CASCADE)
    value = models.FloatField(blank=True, null=True)