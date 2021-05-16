from django.db import models
from django.urls import *

# Create your models here.

class Make(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Model(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Variant(models.Model):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.model.name+' '+self.name

class Car(models.Model):
    make = models.ForeignKey(Make, on_delete=models.SET_NULL, blank=True, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, blank=True, null=True)
    variant = models.ForeignKey(Variant, on_delete=models.SET_NULL, blank=True, null=True)

    image = models.ImageField(upload_to='newcars/', blank=True)
    description = models.TextField()
    year=models.CharField(max_length=4,blank=True, null=True)
    mileage=models.CharField(max_length=20,blank=True, null=True)
    fuel=models.CharField(max_length=20,blank=True, null=True)
    engine_size=models.CharField(max_length=20,blank=True, null=True)
    power=models.CharField(max_length=20,blank=True, null=True)
    gear_box=models.CharField(max_length=20,blank=True, null=True)
    seats=models.CharField(max_length=20,blank=True, null=True)
    doors=models.CharField(max_length=20,blank=True, null=True)
    colors=models.CharField(max_length=100,blank=True, null=True)
    price=models.CharField(max_length=100,blank=True, null=True)

    def remove_on_image_update(self):
        try:
            obj = Car.objects.get(id=self.id)
        except Car.DoesNotExist:
            return
        if obj.image and self.image and obj.image != self.image:
            obj.image.delete()

    def delete(self, *args, **kwargs):
        self.image.delete()
        return super(Car, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.remove_on_image_update()
        return super(Car, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("models:models-detail", kwargs={"id":self.id})
    
    def __str__(self):
        return self.make.name+' '+self.model.name+' '+self.variant.name