from django import forms
from django.core.exceptions import ValidationError
from taxi.models import Driver, Car


class DriverLicenseUpdateForm(forms.ModelForm):
    license_number = forms.CharField(required=True)

    class Meta:
        model = Driver
        fields = ("first_name", "last_name", "license_number")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if len(license_number) != 8:
            raise ValidationError("License number must be exactly 8 characters long")

        first_part = license_number[:3]
        second_part = license_number[3:]

        if not first_part.isupper() or not first_part.isalpha():
            raise ValidationError("First 3 characters must be uppercase letters")

        if not second_part.isdigit():
            raise ValidationError("Last 5 characters must be digits")

        return license_number




class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        widgets = {
            "drivers": forms.CheckboxSelectMultiple()
        }