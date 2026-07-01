from django.contrib import admin
from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "vehicle_number",
        "company",
        "model",
        "fuel_type",
        "customer",
    )

    search_fields = (
        "vehicle_number",
        "company",
        "model",
    )

    list_filter = (
        "company",
        "fuel_type",
    )