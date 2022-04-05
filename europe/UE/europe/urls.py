from django.contrib import admin
from django.urls import path, include, re_path
from europe import views
# from django.conf.urls import url

urlpatterns = [
    path('', views.home, name="home"),
    re_path(r'^economy/gdp/', views.gdp, name="gdp"),
    re_path(r'^economy/gdp_growth/', views.gdp_growth, name="gdp_growth"),
    re_path(r'^economy/gdp_per_capita/', views.gdp_per_capita, name="gdp_per_capita"),
]