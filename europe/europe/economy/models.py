from itertools import count
from django.db import models
from countries.models import Country

# Create your models here.
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