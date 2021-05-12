from django.db import models

from models.models import Car

# Create your models here.
class SellCar(models.Model):
    fullname = models.CharField(max_length= 100, blank=False)
    email = models.EmailField(blank=False)
    STATE_CHOICES = [
        ('', 'SELECT STATE'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Delhi', 'Delhi'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu & Kashmir', 'Jammu & Kashmir'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Orissa', 'Orissa'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttaranchal', 'Uttaranchal'),
        ('West Bengal', 'West Bengal'),
    ]
    state = models.CharField(max_length=50, choices=STATE_CHOICES, default='')
    CITY_CHOICES = [
        ('', 'SELECT CITY'),
        ('Delhi', 'Delhi'),
        ('Mumbai', 'Mumbai'),
        ('Ahmedabad', 'Ahmedabad'),
        ('Bangalore', 'Bangalore'),
        ('Chennai', 'Chennai'),
        ('Chandigarh', 'Chandigarh'),
        ('Coimbatore', 'Coimbatore'),
        ('Gurgaon', 'Gurgaon'),
        ('Hyderabad', 'Hyderabad'),
        ('Jaipur', 'Jaipur'),
        ('Kolkata', 'Kolkata'),
        ('Lucknow', 'Lucknow'),
        ('Noida', 'Noida'),
        ('Thane', 'Thane'),
        ('Patna', 'Patna'),
        ('Pune', 'Pune'),
    ]
    city = models.CharField(max_length=50, choices=CITY_CHOICES, default='')
    MAKE_CHOICES = [
        ('', 'Select Make'),
        ('BENZ', 'Benz'),
        ('AUDI', 'Audi'),
        ('BMW', 'BMW'),
        ('TOYOTA', 'Toyota'),
        ('SUZUKI', 'Suzuki'),
    ]
    make = models.CharField(max_length=20, choices=MAKE_CHOICES, default='')
    NAME_CHOICES = [
        ('', 'Select Model'),
        ('one', 'M1'),
        ('two', 'M2'),
        ('three', 'M3'),
        ('four', 'M4'),
        ('five', 'M5'),
    ]
    name = models.CharField(max_length=50, choices=NAME_CHOICES, default='')
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
    variant = models.CharField(max_length=50, choices=VARIANT_CHOICES, default='')
    year = models.IntegerField()
    kilometer = models.DecimalField(max_digits= 10, decimal_places= 2)
    regno = models.IntegerField()
    expectedprice = models.DecimalField(max_digits= 10, decimal_places= 2)
    DEALER_STATE_CHOICES = [
        ('', 'SELECT STATE'),
        ('Andhra Pradesh', 'Andhra Pradesh'),
        ('Assam', 'Assam'),
        ('Bihar', 'Bihar'),
        ('Chandigarh', 'Chandigarh'),
        ('Chhattisgarh', 'Chhattisgarh'),
        ('Delhi', 'Delhi'),
        ('Gujarat', 'Gujarat'),
        ('Haryana', 'Haryana'),
        ('Himachal Pradesh', 'Himachal Pradesh'),
        ('Jammu & Kashmir', 'Jammu & Kashmir'),
        ('Karnataka', 'Karnataka'),
        ('Kerala', 'Kerala'),
        ('Madhya Pradesh', 'Madhya Pradesh'),
        ('Maharashtra', 'Maharashtra'),
        ('Orissa', 'Orissa'),
        ('Puducherry', 'Puducherry'),
        ('Punjab', 'Punjab'),
        ('Rajasthan', 'Rajasthan'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Telangana', 'Telangana'),
        ('Uttar Pradesh', 'Uttar Pradesh'),
        ('Uttaranchal', 'Uttaranchal'),
        ('West Bengal', 'West Bengal'),
    ]
    dealer_state = models.CharField(max_length=50, choices=DEALER_STATE_CHOICES, default='')
    DEALER_CITY_CHOICES = [
        ('', 'SELECT CITY'),
        ('Delhi', 'Delhi'),
        ('Mumbai', 'Mumbai'),
        ('Ahmedabad', 'Ahmedabad'),
        ('Bangalore', 'Bangalore'),
        ('Chennai', 'Chennai'),
        ('Chandigarh', 'Chandigarh'),
        ('Coimbatore', 'Coimbatore'),
        ('Gurgaon', 'Gurgaon'),
        ('Hyderabad', 'Hyderabad'),
        ('Jaipur', 'Jaipur'),
        ('Kolkata', 'Kolkata'),
        ('Lucknow', 'Lucknow'),
        ('Noida', 'Noida'),
        ('Thane', 'Thane'),
        ('Patna', 'Patna'),
        ('Pune', 'Pune'),
    ]
    dealer_city = models.CharField(max_length=50, choices=DEALER_CITY_CHOICES, default='')
    DEALER_CHOICES = [
        ('', 'SELECT DEALER'),
        ('1','DEALER A'),
        ('2','DEALER B'),
        ('3','DEALER C'),
        ('4','DEALER D'),
        ('5','DEALER E'),
    ]
    dealer = models.CharField(max_length=50, choices=DEALER_CHOICES, default='')