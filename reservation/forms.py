from django import forms
from .models import Reservation


class AvailabilityForm(forms.ModelForm):
    guests = forms.IntegerField(min_value=0)

    class Meta:
        model = Reservation
        fields = ['booking_date', 'booking_time', 'guests']
