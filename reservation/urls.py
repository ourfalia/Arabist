from django.urls import path
from . import views


urlpatterns = [
    path('', views.make_reservation, name='reservation'),
    path('', views.table_list, name='table'),
]
