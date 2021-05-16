from django.db import models

# Create your models here.
from django.db import models

class State(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class User(models.Model):
    firstname = models.CharField(max_length= 50, blank=False)
    lastname = models.CharField(max_length= 50, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length= 50, blank=False)
    mobile = models.CharField(max_length=15, blank=False)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.firstname+' '+self.lastname

class Dealer(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(blank=False)
    mobile = models.CharField(max_length=15, blank=False)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.TextField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
