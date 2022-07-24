from europe.models import *
from rest_framework import routers, serializers, viewsets

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'