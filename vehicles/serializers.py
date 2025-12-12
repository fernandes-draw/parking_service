from rest_framework import serializers
from vehicles.models import VehicleType, Vehicle

class VehiclesTypeSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = VehicleType
    fields = "__all__"
    

class VehiclesSerializer(serializers.ModelSerializer):
    
  class Meta:
    model = Vehicle
    fields = "__all__"