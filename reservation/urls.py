from django.urls import path
from . import views
from .views import TableList, ReservationList, ReservationView, CancelReservation


urlpatterns = [
    path('table_list/', TableList.as_view(), name='TableList'),
    path('reservation_list/', ReservationList.as_view(), name='ReservationList'),
    path('make_reservation', ReservationView.as_view(), name='ReservationView'),
    path('cancel/<pk>',
         CancelReservation.as_view(), name='CancelReservation'),
    path('edit/<int:reservation_id>/',
         views.edit_reservation, name='edit_reservation'),
]
