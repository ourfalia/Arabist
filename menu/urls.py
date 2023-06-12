from django.urls import path
from . import views


urlpatterns = [
    path('', views.meal_list, name='menu'),
    path('<int:meal_id>/', views.meal_detail, name='meal_detail'),
]
