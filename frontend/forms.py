from django import forms
from django.contrib.admin import widgets

from .models import BookingRequest


class CustomAdminDateWidget(widgets.AdminDateWidget):
    def __init__(self, attrs=None):
        final_attrs = {"class": "form-control", "type": "datetime-local"}
        if attrs is not None:
            final_attrs.update(attrs)
        super().__init__(attrs=final_attrs)


class CustomInputWidget(widgets.AdminTextInputWidget):
    def __init__(self, attrs=None):
        final_attrs = {"class": "form-control"}
        if attrs is not None:
            final_attrs.update(attrs)
        super().__init__(attrs=final_attrs)


class BookingRequestForm(forms.ModelForm):
    booked_from = forms.DateTimeField(
        label="Select booking start date", widget=CustomAdminDateWidget
    )
    booked_till = forms.DateTimeField(
        label="Select booking end date", widget=CustomAdminDateWidget
    )
    customer_name = forms.CharField(label="Enter your name", widget=CustomInputWidget)
    customer_email = forms.EmailField(
        label="Enter your email", widget=CustomInputWidget(attrs={"type": "email"})
    )
    customer_address = forms.CharField(label="Address", widget=CustomInputWidget)
    customer_contact = forms.CharField(label="Contact number", widget=CustomInputWidget)

    class Meta:
        model = BookingRequest
        exclude = ["hall", "status"]
