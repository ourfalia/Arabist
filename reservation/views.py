from django.shortcuts import render
from django.views.generic import ListView

from .models import Table, Reservation

# Create your views here.


class TableList(ListView):
    model = Table


class ReservationList(ListView):
    model = Reservation
