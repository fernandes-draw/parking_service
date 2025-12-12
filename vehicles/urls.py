from django.urls import path, include
from rest_framework.routers import DefaultRouter

from vehicles.views import VehiclesViewSet, VehiclesTypeViewSet

router = DefaultRouter()
router.register("vehicles/type", VehiclesTypeViewSet)
router.register("vehicles", VehiclesViewSet)


urlpatterns = [
    path("", include(router.urls))
]
