from django.db import models

from home.models import State, City, Dealer
from models.models import Make, Model, Variant
from django.db import models

# Create your models here.
class SellCar(models.Model):
    fullname = models.CharField(max_length= 100, blank=False)
    email = models.EmailField(blank=False)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    make = models.ForeignKey(Make, on_delete=models.SET_NULL, blank=True, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, blank=True, null=True)
    variant = models.ForeignKey(Variant, on_delete=models.SET_NULL, blank=True, null=True)
    year = models.IntegerField()
    kilometer = models.DecimalField(max_digits= 10, decimal_places= 2)
    regno = models.IntegerField()
    expectedprice = models.DecimalField(max_digits= 10, decimal_places= 2)
    dealer = models.ForeignKey(Dealer, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.fullname+' '+self.regno+' '+self.make+' '+self.model+' '+self.variant
