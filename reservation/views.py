from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, FormView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime

from .models import Table, Reservation
from .forms import AvailabilityForm

# Create your views here.


class TableList(ListView):
    model = Table


class ReservationList(ListView):
    model = Reservation
    template_name = "reservation_list.html"

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            reservation_list = Reservation.objects.all()
            return reservation_list
        else:
            reservation_list = Reservation.objects.filter(
                user=self.request.user)
            return reservation_list


class ReservationView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        table_list = Table.objects.all()
        available_tables = []
        for table in table_list:
            if check_availability(table, data['booking_date'], data['booking_time'], data['guests']):
                available_tables.append(table)

        if len(available_tables) > 0:
            table = available_tables[0]
            reservation = Reservation.objects.create(
                user=self.request.user,
                table=table,
                booking_date=data['booking_date'],
                booking_time=data['booking_time'],
                guests=data['guests']
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('No tables available')


def check_availability(table, booking_date, booking_time, guests):
    avail_list = []
    reservation_list = Reservation.objects.filter(table=table)
    for reservation in reservation_list:
        if reservation.booking_date == booking_date and reservation.booking_time == booking_time:
            avail_list.append(False)
    return all(avail_list)


class CancelReservation(DeleteView):
    model = Reservation
    template_name = 'cancel_view.html'
    success_url = reverse_lazy('reservation:ReservationList')
