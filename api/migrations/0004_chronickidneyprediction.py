# Generated by Django 3.2.13 on 2023-10-09 18:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_heartdisease_prediction_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChronicKidneyPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bp', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(50), django.core.validators.MaxValueValidator(180)])),
                ('Sg', models.FloatField(validators=[django.core.validators.MinValueValidator(1.005), django.core.validators.MaxValueValidator(1.025)])),
                ('Al', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('Su', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('Rbc', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Bu', models.FloatField(validators=[django.core.validators.MinValueValidator(1.5), django.core.validators.MaxValueValidator(391.0)])),
                ('Sc', models.FloatField(validators=[django.core.validators.MinValueValidator(0.4), django.core.validators.MaxValueValidator(76.0)])),
                ('Sod', models.FloatField(validators=[django.core.validators.MinValueValidator(4.5), django.core.validators.MaxValueValidator(163.0)])),
                ('Pot', models.FloatField(validators=[django.core.validators.MinValueValidator(2.5), django.core.validators.MaxValueValidator(47.0)])),
                ('Hemo', models.FloatField(validators=[django.core.validators.MinValueValidator(3.1), django.core.validators.MaxValueValidator(17.8)])),
                ('Wbcc', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2200), django.core.validators.MaxValueValidator(26400)])),
                ('Rbcc', models.FloatField(validators=[django.core.validators.MinValueValidator(2.1), django.core.validators.MaxValueValidator(8.0)])),
                ('Htn', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('Class', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)])),
                ('prediction', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('prediction_message', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
