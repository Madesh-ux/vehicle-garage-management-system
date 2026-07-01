from django.db import models

# Create your models here.
from vehicles.models import Vehicle

class Booking(models.Model):

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    SERVICE_CHOICES = [
    ("Oil Change", "Oil Change"),
    ("Water Wash", "Water Wash"),
    ("General Service", "General Service"),
    ("Brake Service", "Brake Service"),
]

    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)

    booking_date = models.DateField()

    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.service_type