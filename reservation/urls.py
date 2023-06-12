from django.urls import path
from . import views
from .views import ReservationList, ReservationView

# , CancelReservation


urlpatterns = [
    path('reservation_list/', ReservationList.as_view(), name='ReservationList'),
    path('make_reservation/', ReservationView.as_view(), name='ReservationView'),
    path('delete/<int:reservation_id>/',
         views.cancel_reservation, name='cancel_reservation'),
    path('edit/<int:reservation_id>/',
         views.edit_reservation, name='edit_reservation'),
]
