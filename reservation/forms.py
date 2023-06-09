from django import forms
from .models import Reservation


class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['booking_date', 'booking_time', 'guests']
