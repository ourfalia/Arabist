from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import get_object_or_404
from menu.models import Meals


class MealViewsTestCase(TestCase):

    def test_meal_list(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/all_meals.html')

    def setUp(self):
        self.client = Client()
        # Create a sample meal object with an image
        self.meal = Meals.objects.create(
            name='Meal 1',
            description='Description 1',
            price=9.99,
            image='path/to/image.jpg'
        )

    def test_meal_detail(self):
        # Retrieve the URL using the named URL pattern and pass the meal ID
        url = reverse('meal_detail', args=[self.meal.pk])

        # Send a GET request to the URL
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response uses the expected template
        self.assertTemplateUsed(response, 'menu/meal_detail.html')

        # Assert that the 'meal' context variable is passed to the template
        meal = response.context['meal']
        self.assertIsNotNone(meal)
        self.assertEqual(meal, self.meal)

        # Assert that the meal name, description, price, and image are present in the rendered response
        self.assertContains(response, 'Meal 1')
        self.assertContains(response, 'Description 1')
        self.assertContains(response, '9.99')
        self.assertContains(response, 'path/to/image.jpg')

    def test_meal_detail_not_found(self):
        # Retrieve a non-existent meal ID
        non_existent_meal_id = 9999

        # Retrieve the URL using the named URL pattern and pass the non-existent meal ID
        url = reverse('meal_detail', args=[non_existent_meal_id])

        # Send a GET request to the URL
        response = self.client.get(url)

        # Assert that the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)
