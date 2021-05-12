from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length= 50, blank=False)
    lastname = models.CharField(max_length= 50, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length= 50, blank=False)
    mobile = models.CharField(max_length=15, blank=False)

class Dealer(User, models.Model):
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
    state = models.CharField(
        max_length=50,
        choices=STATE_CHOICES,
        default='',
    )
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
    city = models.CharField(
        max_length=50,
        choices=CITY_CHOICES,
        default='',
    )