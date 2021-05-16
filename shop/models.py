from django.db import models

from home.models import State, City, Dealer
from models.models import Make, Model, Variant
from django.db import models

# Create your models here.
class SellCar(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    make = models.ForeignKey(Make, on_delete=models.SET_NULL, blank=True, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, blank=True, null=True)
    variant = models.ForeignKey(Variant, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='shop/', blank=True)
    description = models.TextField()
    year = models.CharField(max_length=4, blank=True, null=True)
    mileage = models.CharField(max_length=20, blank=True, null=True)
    fuel = models.CharField(max_length=20, blank=True, null=True)
    engine_size = models.CharField(max_length=20, blank=True, null=True)
    power = models.CharField(max_length=20, blank=True, null=True)
    gear_box = models.CharField(max_length=20, blank=True, null=True)
    seats = models.CharField(max_length=20, blank=True, null=True)
    doors = models.CharField(max_length=20, blank=True, null=True)
    colors = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    kilometer = models.CharField(max_length=100, blank=True, null=True)
    reg_no = models.CharField(max_length=20, blank=True, null=True)

    def remove_on_image_update(self):
        try:
            obj = SellCar.objects.get(id=self.id)
        except SellCar.DoesNotExist:
            return
        if obj.image and self.image and obj.image != self.image:
            obj.image.delete()

    def delete(self, *args, **kwargs):
        self.image.delete()
        return super(SellCar, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.remove_on_image_update()
        return super(SellCar, self).save(*args, **kwargs)

    def __str__(self):
        return self.fullname+' '+str(self.reg_no)+' '+str(self.make)+' '+str(self.model)+' '+str(self.variant)
