# from django.db import models
#
# from home.models import User
#
# # Create your models here.
# class SellCar(models.Model):
#     firstname = models.CharField(max_length= 50, blank=False)
#     lastname = models.CharField(max_length= 50, blank=False)
#     email = models.EmailField(blank=False)
#     mobile = models.CharField(max_length=15, blank=False)
#
# class Car(models.Model):
#     #make
#     #name
#     #variant
#     image = models.ImageField(upload_to='shop/static/images/', blank=True)
#     description = models.TextField()
#     year = models.IntegerField()
#     kilometer = models.DecimalField()
#     regno = models.PositiveBigIntegerField()
#     expectedprice = models.DecimalField()
#
# class Dealer(User, models.Model):
#     #state
#     #city
#     pass
#
#
# class Sport(models.Model):
#     MAKE = ''
#     BENZ = 'Mercedes-Benz'
#     AUDI = 'Audi'
#     BMW = 'BMW'
#     TOYOTA = 'Toyota'
#     SUZUKI = 'Maruthi Suzuki'
#     MAKE_CHOICES = [
#         ('', 'Select Make'),
#         (BENZ, 'Benz'),
#         (AUDI, 'Audi'),
#         (BMW, 'BMW'),
#         (TOYOTA, 'Toyota'),
#         (SUZUKI, 'Suzuki'),
#     ]
#     make = models.CharField(
#         max_length=20,
#         choices=MAKE_CHOICES,
#         default=MAKE,
#     )
#     name = models.CharField(max_length=100)
#     image = models.ImageField(blank=True)
#     description = models.TextField()
#
#     def str(self):
#         return self.name