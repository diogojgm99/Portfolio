from django.db import models
import  europe.settings as s
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    sigla = models.CharField(max_length=5, default="")
    population = models.IntegerField(default=0)
    currency = models.CharField(max_length=50,default="Euro")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Country"

class GDP(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    year = models.IntegerField()
    gdp = models.IntegerField(default=0)

    def __str__(self):
        label = "{} - {} - {}".format(self.country, self.year, self.gdp)
        return label

    class Meta:
        verbose_name = "GDP"
        verbose_name_plural = "GDP"

class GDP_per_capita(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    year = models.IntegerField()
    gdp_per_capita = models.IntegerField(default=0)

    def __str__(self):
        label = "{} - {} - {}".format(self.country, self.year, self.gdp_per_capita)
        return label
    
    class Meta:
        verbose_name = "GDP_per_capita"
        verbose_name_plural = "GDP_per_capita"

class GDP_Growth(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    year = models.IntegerField()
    gdp_growth = models.FloatField(default=0)

    def __str__(self):
        label = "{} - {} - {}".format(self.country, self.year, self.gdp_growth)
        return label
    
    class Meta:
        verbose_name = "GDP_Growth"
        verbose_name_plural = "GDP_Growth"


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
    report = models.ForeignKey(Tag, on_delete= models.CASCADE)
    menu = models.CharField(max_length = 255, choices = s.MENUS, default = "Economy")

    def __str__(self):
        return self.name