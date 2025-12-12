from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from vehicles.models import VehicleType, Vehicle
from vehicles.serializers import VehiclesTypeSerializer, VehiclesSerializer

class VehiclesTypeViewSet(viewsets.ModelViewSet):
  queryset = VehicleType.objects.all()
  serializer_class = VehiclesTypeSerializer
  
  
class VehiclesViewSet(viewsets.ModelViewSet):
  queryset = Vehicle.objects.all()
  serializer_class = VehiclesSerializer
  
