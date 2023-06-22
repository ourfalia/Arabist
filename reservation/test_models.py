from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Table, Reservation

User = get_user_model()


class TableModelTest(TestCase):
    def test_table_creation(self):
        table = Table.objects.create(number=1)
        self.assertEqual(table.number, 1)
        self.assertEqual(str(table), "Table number 1")


class ReservationModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.table = Table.objects.create(number=1)
        self.reservation = Reservation.objects.create(
            user=self.user,
            table=self.table,
            booking_date="2023-06-30",
            booking_time="19:00",
            guests=4,
        )

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.user, self.user)
        self.assertEqual(self.reservation.table, self.table)
        self.assertEqual(self.reservation.booking_date, "2023-06-30")
        self.assertEqual(self.reservation.booking_time, "19:00")
        self.assertEqual(self.reservation.guests, 4)
        self.assertEqual(
            str(self.reservation),
            f"testuser has booked table number 1 on 2023-06-30 at 19:00",
        )
