# Generated by Django 3.0.5 on 2021-05-17 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellcar',
            name='colors',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='doors',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='engine_size',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='fuel',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='gear_box',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='kilometer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='mileage',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='power',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='reg_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='seats',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='sellcar',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
