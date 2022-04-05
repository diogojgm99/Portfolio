from urllib import request
from django.shortcuts import render
import europe.utils as u
import logging


# Create your views here.
def home(request):
    # Get menus and reports for sidebar
    menus = u.get_menus_reports()
    submenus = u.get_submenus(menus)
    context = {
        'menus': menus,
        'submenus': submenus,
    }
    return render(request, "home.html", context)

# def economy(request):
#     return render(request, "gdp.html", context)

def gdp(request):
    menus = u.get_menus_reports()
    submenus = u.get_submenus(menus)
    context = {
        'menus': menus,
        'submenus': submenus,
    }
    return render(request, "economy/gdp.html", context)

def gdp_growth(request):
    menus = u.get_menus_reports()
    submenus = u.get_submenus(menus)
    context = {
        'menus': menus,
        'submenus': submenus,
    }
    return render(request, "economy/gdp_growth.html", context)

def gdp_per_capita(request):
    menus = u.get_menus_reports()
    submenus = u.get_submenus(menus)
    context = {
        'menus': menus,
        'submenus': submenus,
    }
    return render(request, "economy/gdp_per_capita.html", context)