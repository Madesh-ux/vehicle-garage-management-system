from django import forms
from .models import Customer


class CustomerRegistrationForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = [
            "full_name",
            "email",
            "phone",
            "password",
            "address",
        ]

        widgets = {
            "password": forms.PasswordInput(),
        }