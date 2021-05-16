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
    car_main_Img = models.ImageField(upload_to='shop/', blank=True)

    def remove_on_image_update(self):
        try:
            obj = SellCar.objects.get(id=self.id)
        except SellCar.DoesNotExist:
            return
        if obj.car_main_Img and self.car_main_Img and obj.car_main_Img != self.car_main_Img:
            obj.car_main_Img.delete()

    def delete(self, *args, **kwargs):
        self.car_main_Img.delete()
        return super(SellCar, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.remove_on_image_update()
        return super(SellCar, self).save(*args, **kwargs)

    def __str__(self):
        return self.fullname+' '+str(self.regno)+' '+str(self.make)+' '+str(self.model)+' '+str(self.variant)
