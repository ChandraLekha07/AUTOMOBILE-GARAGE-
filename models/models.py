from django.db import models

# Create your models here.
class Car(models.Model):
    MAKE_CHOICES = [
        ('', 'Select Make'),
        ('BENZ', 'Benz'),
        ('AUDI', 'Audi'),
        ('BMW', 'BMW'),
        ('TOYOTA', 'Toyota'),
        ('SUZUKI', 'Suzuki'),
    ]
    make = models.CharField(
        max_length=20,
        choices=MAKE_CHOICES,
        default='',
    )
    NAME_CHOICES = [
        ('', 'Select Model'),
        ('one', 'M1'),
        ('two', 'M2'),
        ('three', 'M3'),
        ('four', 'M4'),
        ('five', 'M5'),
    ]
    name = models.CharField(
        max_length=50,
        choices=NAME_CHOICES,
        default='',
    )
    VARIANT_CHOICES = [
        ('', 'Select Variant'),
        ('sedan', 'SEDAN'),
        ('coupe', 'COUPE'),
        ('sports', 'SPORTS CAR'),
        ('stationwagon', 'STATION WAGON'),
        ('hatchback', 'HATCHBACK'),
        ('convertible', 'CONVERTIBLE'),
        ('suv', 'SPORT-UTILITY VEHICLE (SUV)'),
        ('minivan', 'MINIVAN'),
        ('pickup', ' PICKUP TRUCK'),
    ]
    variant = models.CharField(
        max_length=50,
        choices=VARIANT_CHOICES,
        default='',
    )
    image = models.ImageField(upload_to='models/static/images/', blank=True)
    description = models.TextField()
