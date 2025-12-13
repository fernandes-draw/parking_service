from core.permissions import IsOwnerOfVehicleOrRecord
from rest_framework import viewsets
from vehicles.models import VehicleType, Vehicle
from vehicles.serializers import VehiclesTypeSerializer, VehiclesSerializer
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser


class VehiclesTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehiclesTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehiclesSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Vehicle.objects.all()

        return Vehicle.objects.filter(owner__user=user)
