from django.shortcuts import render
from rest_framework import viewsets

from .models import ShoeType, ShoeColor, Shoe
from manufacturer.models import Manufacturer
from .serializers import ShoeSerializer, ShoeColorSerializer, ShoeTypeSerializer, ManufacturerSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer

class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer