# Generated by Django 3.0.5 on 2021-05-17 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_messages'),
        ('shop', '0005_auto_20210517_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.SellCar')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.User')),
            ],
        ),
    ]
