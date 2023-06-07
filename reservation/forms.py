from django import forms


class AvailabilityForm(forms.Form):
    booking_date = forms.DateField(required=True)
    booking_time = forms.TimeField(required=True)
    guests = forms.DecimalField(required=True)
