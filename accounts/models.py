from django.db import models

# Create your models here.
class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.full_name
