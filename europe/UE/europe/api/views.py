from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
import logging
from rest_framework.renderers import JSONRenderer
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.db.models import Max
from rest_framework.views import APIView
from europe.models import Country
from europe.api.serializers import CountrySerializer

logger = logging.getLogger(__name__)


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    def get_queryset(self):
        queryset = Country.objects.all()
        name = self.request.query_params.get('name', None)
        code = self.request.query_params.get('code', None)
        currency = self.request.query_params.get('currency', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        if code is not None:
            queryset = queryset.filter(code=code)
        if currency is not None:
            queryset = queryset.filter(currency=currency)
        return queryset
