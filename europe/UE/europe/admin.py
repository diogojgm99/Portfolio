from django.contrib import admin
from .models import *

# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('group',)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

class DataReportAdmin(admin.ModelAdmin):
    list_display = ("country", "report", "year", "value")
    list_filter = ('country','report__name','year')

# Register your models here.
admin.site.register(Country, CountryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Data_report, DataReportAdmin)