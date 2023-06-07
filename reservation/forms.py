from django import forms


class AvailabilityForm(forms.Form):
    booking_time = forms.DateTimeField(required=True)
    guests = forms.DecimalField(required=True)
