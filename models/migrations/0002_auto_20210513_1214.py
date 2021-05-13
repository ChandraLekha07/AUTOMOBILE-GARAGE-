# Generated by Django 3.0.5 on 2021-05-13 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Make')),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='name',
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Make')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Model')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.Model'),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.Make'),
        ),
        migrations.AlterField(
            model_name='car',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.Variant'),
        ),
    ]
