from django.test import TestCase
from django.utils.html import strip_tags
from .forms import AvailabilityForm


class AvailabilityFormTest(TestCase):
    def test_valid_form(self):
        # Create form data with valid values
        form_data = {
            'booking_date': '2023-06-30',
            'booking_time': '19:00',
            'guests': 4,
        }

        form = AvailabilityForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Create form data with invalid values
        form_data = {
            'booking_date': '',  # Empty date
            'booking_time': '19:00',
            'guests': -2,  # Negative number of guests
        }

        form = AvailabilityForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Check for expected errors
        expected_errors = {
            'booking_date': 'This field is required.',
            'guests': 'Ensure this value is greater than or equal to 0.',
        }

        for field, expected_error in expected_errors.items():
            actual_error = form.errors.get(field)
            actual_error_text = strip_tags(str(actual_error))
            self.assertEqual(actual_error_text, expected_error,
                             f"Unexpected error for field '{field}'")

    def test_form_fields(self):
        form = AvailabilityForm()
        self.assertEqual(list(form.fields.keys()), [
            'booking_date', 'booking_time', 'guests'])
