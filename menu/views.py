from django.shortcuts import render, get_object_or_404
from .models import Meals
# Create your views here.


def meal_list(request):
    meals = Meals.objects.all()
    context = {
        'meals': meals,
    }

    return render(request, 'menu/all_meals.html', context)


def meal_detail(request, meal_id):
    meal = get_object_or_404(Meals, pk=meal_id)

    context = {
        'meal': meal,
    }

    return render(request, 'menu/meal_detail.html', context)
