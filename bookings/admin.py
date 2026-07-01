from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "vehicle",
        "service_type",
        "booking_date",
        "status",
    )

    search_fields = (
        "vehicle__vehicle_number",
        "service_type",
    )

    list_filter = (
        "status",
        "service_type",
    )