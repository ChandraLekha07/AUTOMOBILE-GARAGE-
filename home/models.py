from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length= 50, blank=False)
    lastname = models.CharField(max_length= 50, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length= 50, blank=False)
    mobile = models.CharField(max_length=15, blank=False)
