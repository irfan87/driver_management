from django.db import models


class Driver(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    plate_number = models.CharField(max_length=50)
    loading_capacity = models.CharField(max_length=50)
    drived_by = models.ForeignKey(Driver, on_delete=models.CASCADE)

    def __str__(self):
        return self.plate_number
