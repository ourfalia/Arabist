from django.test import TestCase
from menu.models import Meals


class MealsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Meals.objects.create(
            name='Burger',
            description='A delicious burger',
            price=9.99,
            image='menu/burger.jpg'
        )

    def test_name_label(self):
        meal = Meals.objects.get(id=1)
        field_label = meal._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        meal = Meals.objects.get(id=1)
        field_label = meal._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_price_label(self):
        meal = Meals.objects.get(id=1)
        field_label = meal._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_image_label(self):
        meal = Meals.objects.get(id=1)
        field_label = meal._meta.get_field('image').verbose_name
        self.assertEquals(field_label, 'image')

    def test_name_max_length(self):
        meal = Meals.objects.get(id=1)
        max_length = meal._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_description_max_length(self):
        meal = Meals.objects.get(id=1)
        max_length = meal._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    def test_price_decimal_places(self):
        meal = Meals.objects.get(id=1)
        decimal_places = meal._meta.get_field('price').decimal_places
        self.assertEquals(decimal_places, 2)

    def test_price_max_digits(self):
        meal = Meals.objects.get(id=1)
        max_digits = meal._meta.get_field('price').max_digits
        self.assertEquals(max_digits, 5)
