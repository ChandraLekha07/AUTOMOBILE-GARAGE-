# Generated by Django 3.0.5 on 2021-05-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('otp', models.CharField(max_length=6)),
                ('state', models.CharField(choices=[('', 'SELECT STATE'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Delhi', 'Delhi'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Orissa', 'Orissa'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttaranchal', 'Uttaranchal'), ('West Bengal', 'West Bengal')], default='', max_length=50)),
                ('city', models.CharField(choices=[('', 'SELECT CITY'), ('Delhi', 'Delhi'), ('Mumbai', 'Mumbai'), ('Ahmedabad', 'Ahmedabad'), ('Bangalore', 'Bangalore'), ('Chennai', 'Chennai'), ('Chandigarh', 'Chandigarh'), ('Coimbatore', 'Coimbatore'), ('Gurgaon', 'Gurgaon'), ('Hyderabad', 'Hyderabad'), ('Jaipur', 'Jaipur'), ('Kolkata', 'Kolkata'), ('Lucknow', 'Lucknow'), ('Noida', 'Noida'), ('Thane', 'Thane'), ('Patna', 'Patna'), ('Pune', 'Pune')], default='', max_length=50)),
                ('make', models.CharField(choices=[('', 'Select Make'), ('BENZ', 'Benz'), ('AUDI', 'Audi'), ('BMW', 'BMW'), ('TOYOTA', 'Toyota'), ('SUZUKI', 'Suzuki')], default='', max_length=20)),
                ('name', models.CharField(choices=[('', 'Select Model'), ('one', 'M1'), ('two', 'M2'), ('three', 'M3'), ('four', 'M4'), ('five', 'M5')], default='', max_length=50)),
                ('variant', models.CharField(choices=[('', 'Select Variant'), ('sedan', 'SEDAN'), ('coupe', 'COUPE'), ('sports', 'SPORTS CAR'), ('stationwagon', 'STATION WAGON'), ('hatchback', 'HATCHBACK'), ('convertible', 'CONVERTIBLE'), ('suv', 'SPORT-UTILITY VEHICLE (SUV)'), ('minivan', 'MINIVAN'), ('pickup', ' PICKUP TRUCK')], default='', max_length=50)),
                ('year', models.IntegerField()),
                ('kilometer', models.DecimalField(decimal_places=2, max_digits=10)),
                ('regno', models.BigIntegerField()),
                ('expectedprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dealer_state', models.CharField(choices=[('', 'SELECT STATE'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chandigarh', 'Chandigarh'), ('Chhattisgarh', 'Chhattisgarh'), ('Delhi', 'Delhi'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Orissa', 'Orissa'), ('Puducherry', 'Puducherry'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttaranchal', 'Uttaranchal'), ('West Bengal', 'West Bengal')], default='', max_length=50)),
                ('dealer_city', models.CharField(choices=[('', 'SELECT CITY'), ('Delhi', 'Delhi'), ('Mumbai', 'Mumbai'), ('Ahmedabad', 'Ahmedabad'), ('Bangalore', 'Bangalore'), ('Chennai', 'Chennai'), ('Chandigarh', 'Chandigarh'), ('Coimbatore', 'Coimbatore'), ('Gurgaon', 'Gurgaon'), ('Hyderabad', 'Hyderabad'), ('Jaipur', 'Jaipur'), ('Kolkata', 'Kolkata'), ('Lucknow', 'Lucknow'), ('Noida', 'Noida'), ('Thane', 'Thane'), ('Patna', 'Patna'), ('Pune', 'Pune')], default='', max_length=50)),
                ('dealer', models.CharField(choices=[('', 'SELECT DEALER'), ('1', 'DEALER A'), ('2', 'DEALER B'), ('3', 'DEALER C'), ('4', 'DEALER D'), ('5', 'DEALER E')], default='', max_length=50)),
            ],
        ),
    ]
