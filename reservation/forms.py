from django import forms


class AvailabilityForm(forms.form):
    booking_time = forms.DateTimeField(required=True)
