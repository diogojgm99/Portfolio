from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet, basename="countries")
#Criar um endpoint para cada tipo de report


urlpatterns = [
    path('', include(router.urls)),
]