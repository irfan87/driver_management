from rest_framework import serializers
from .models import Driver, Vehicle


# this is where it's begin where the Driver and Vehicle, we convert as the serializer to pass as a JSON 
class DriverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'name', 'phone_number', 'url') 

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'plate_number', 'loading_capacity', 'drived_by', 'url')