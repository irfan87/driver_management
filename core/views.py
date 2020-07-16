from django.shortcuts import render

from rest_framework import viewsets, permissions

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer

# from models and serializers, we use these both as the views
class DriverViews(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class VehicleViews(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



    