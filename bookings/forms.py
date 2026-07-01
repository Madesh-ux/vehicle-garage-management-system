from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ["vehicle", "service_type", "booking_date"]

        widgets = {
            "booking_date": forms.DateInput(attrs={"type": "date"})
        }