from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Reservation, Table


class ReservationViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.table = Table.objects.create(number=1)

    def test_ReservationList_superuser(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('ReservationList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation/reservation_list.html')

    def test_ReservationList_regular_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('ReservationList'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation/reservation_list.html')

    def test_ReservationView_valid_form(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'booking_date': '2023-07-23',
            'booking_time': '18:00:00',
            'guests': 4
        }
        response = self.client.post(reverse('ReservationView'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('ReservationList'))

    def test_ReservationView_no_tables_available(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'booking_date': '2023-07-23',
            'booking_time': '18:00:00',
            'guests': 4
        }
        response = self.client.post(reverse('ReservationView'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('ReservationList'))

    def test_cancel_reservation(self):
        self.client.login(username='testuser', password='testpassword')
        reservation = Reservation.objects.create(
            user=self.user, table=self.table, booking_date='2023-07-23', booking_time='18:00:00', guests=4)
        response = self.client.post(
            reverse('cancel_reservation', args=[reservation.id]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('ReservationList'))

    def test_edit_reservation_valid_form(self):
        self.client.login(username='testuser', password='testpassword')
        reservation = Reservation.objects.create(
            user=self.user, table=self.table, booking_date='2023-07-23', booking_time='18:00:00', guests=4)
        data = {
            'booking_date': '2023-07-24',
            'booking_time': '19:00:00',
            'guests': 6
        }
        response = self.client.post(
            reverse('edit_reservation', args=[reservation.id]), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('ReservationList'))
