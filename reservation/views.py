from django.shortcuts import render
from django.views.generic import ListView, FormView
import datetime

from .models import Table, Reservation
from .forms import AvailabilityForm

# Create your views here.


class TableList(ListView):
    model = Table


class ReservationList(ListView):
    model = Reservation


# class ReservationView(FormView):
#     form_class = AvailabilityForm
#     template_name = 'availability_form.html'

#     def form_valid(self, form):
#         data = form.cleaned_data


def check_availability(table, booking_time):
    avail_list = []
    reservation_list = Reservation.objects.filter(table=table)
    for reservation in reservation_list:
        if reservation.booking_time == booking_time:
            avail_list.append(False)
        else:
            avail_list.append(True)
    return all(avail_list)
