from europe.models import Tag, Country,Report#, GDP, GDP_per_capita, GDP_Growth
import europe.settings as s
import logging

logger = logging.getLogger(__name__)

def get_menus_reports():
    menus = Tag.objects.filter(group="Menu")
    dict_menus = []
    for menu in menus:
        reports = list(Report.objects.filter(menu = menu))
    reports = Report.objects.all()
    return menus

def get_submenus(menus):
    submenus={}
    for menu in menus:
        reports=Report.objects.filter(menu=menu.name).values_list("name", flat=True)
        submenus[menu]=list(reports)
    return submenus

def get_all_countries():
    countries = list(Country.objects.order_by("name").values_list('name',flat=True))
    return countries
