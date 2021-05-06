from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length= 50)
    lastname = models.CharField(max_length= 50)
    email = models.EmailField(validators= [])
    password = models.CharField(max_length= 50)
    mobile = models.CharField(max_length=15)
