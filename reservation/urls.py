from django.urls import path
from . import views
from .views import TableList, ReservationList, ReservationView, CancelReservation

app_name = 'reservation'

urlpatterns = [
    path('table_list/', TableList.as_view(), name='TableList'),
    path('reservation_list/', ReservationList.as_view(), name='ReservationList'),
    path('reservation', ReservationView.as_view(), name='ReservationView'),
    path('reservation/cancel/<pk>',
         CancelReservation.as_view(), name='CancelReservation')
]
