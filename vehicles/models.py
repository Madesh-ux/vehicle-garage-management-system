from django.db import models
from accounts.models import Customer

class Vehicle(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    vehicle_number = models.CharField(max_length=20)

    company = models.CharField(max_length=50)

    model = models.CharField(max_length=50)

    fuel_type = models.CharField(max_length=20)

    def __str__(self):
        return self.vehicle_number