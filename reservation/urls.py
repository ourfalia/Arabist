from django.urls import path
from .views import TableList, ReservationList, ReservationView


urlpatterns = [
    path('table_list', TableList.as_view(), name='TableList'),
    path('reservation_list', ReservationList.as_view(), name='ReservationList'),
    path('reservation', ReservationView.as_view(), name='ReservationView'),
]
