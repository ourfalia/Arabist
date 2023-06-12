from django.db import models

# Create your models here.


class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='menu/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'
