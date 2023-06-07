from django.db import models
from django.conf import settings

# Create your models here.


class Table(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return f'Table number {self.number}'


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    guests = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return f'{self.user} has booked table numer {self.table.number} on {self.booking_date} at {self.booking_time}'
