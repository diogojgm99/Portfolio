from django.contrib import admin
from .models import *

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'population')
    list_filter = ('name',)

class GDPAdmin(admin.ModelAdmin):
    list_display = ('country', 'year' , 'gdp')
    list_filter = ('country','year')

class GDPCapitaAdmin(admin.ModelAdmin):
    list_display = ('country', 'year' , 'gdp_per_capita')
    list_filter = ('country','year')

class GDPGrowthAdmin(admin.ModelAdmin):
    list_display = ('country', 'year' , 'gdp_growth')
    list_filter = ('country','year')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('name' , 'report')
    list_filter = ('name',)

# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(GDP, GDPAdmin)
admin.site.register(GDP_per_capita, GDPCapitaAdmin)
admin.site.register(GDP_Growth, GDPGrowthAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Report, ReportAdmin)