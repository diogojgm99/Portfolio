from urllib import request
from django.shortcuts import render
from europe.models import Report
import europe.utils as u
import logging
import europe.settings as s
from django.http import HttpResponse
import json
import random

logger = logging.getLogger(__name__)

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

# def gdp(request):
#     menus = u.get_menus_reports()
#     submenus = u.get_submenus(menus)
#     countries = u.get_all_countries()
#     reports = Report.objects.filter(name=s.GDP)
#     try:
#         country = request.COOKIES['country']
#     except:
#         country= ""
#     if country == "all":
#         gdp_data = GDP.objects.all().order_by("year")
#     else:
#         gdp_data = GDP.objects.order_by("year").filter(country__name=country)
#     context = {
#         'menus': menus,
#         'submenus': submenus,
#         'countries': countries,
#         'reports': reports,
#         'gdp_data': gdp_data
#     }
#     return render(request, "economy/gdp.html", context)

# def get_gdp_data(request):
#     labels=["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
#     try:
#         country = request.COOKIES['country']
#         type_chart = request.COOKIES['type']
#     except:
#         country = ""
#         type_chart = ""
#     data=""
#     datasets=[]
#     if country == "all":
#         countries = u.get_all_countries()
#         for country in countries:
#             data = list(GDP.objects.order_by("year").filter(country__name=country).values_list("gdp", flat=True))
#             r = lambda: random.randint(0,255)
#             color = "#%02X%02X%02X" % (r(),r(),r())
#             logger.info(color)
#             datasets.append({
#                 'label': country,
#                 'data': data,
#                 'fill': False,
#                 'borderColor': color
#             })
#     else:
#         data = list(GDP.objects.order_by("year").filter(country__name=country).values_list("gdp", flat=True))
#         datasets=[{
#             'label': "GDP",
#             'data': data,
#             'fill': False,
#             'borderColor': "#00A300"
#         }]

#     to_json = {
#         'labels':labels,
#         'datasets':datasets
#     }
#     return HttpResponse(
#             json.dumps(to_json),
#             content_type="application/json"
#         )

# def gdp_growth(request):
#     menus = u.get_menus_reports()
#     submenus = u.get_submenus(menus)
#     context = {
#         'menus': menus,
#         'submenus': submenus,
#     }
#     return render(request, "economy/gdp_growth.html", context)

# def gdp_per_capita(request):
    menus = u.get_menus_reports()
    submenus = u.get_submenus(menus)
    context = {
        'menus': menus,
        'submenus': submenus,
    }
    return render(request, "economy/gdp_per_capita.html", context)