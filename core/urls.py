from django.urls import path, include
from rest_framework import routers

from .views import DriverViews, VehicleViews

# register both DriverViews and VehicleViews for routing
router = routers.DefaultRouter()
router.register('drivers', DriverViews)
router.register('vehicles', VehicleViews)

# define all HTTPs method (POST, GET, PUT, PATCH, DELETE)
urlpatterns = [
    path('', include(router.urls)),
]