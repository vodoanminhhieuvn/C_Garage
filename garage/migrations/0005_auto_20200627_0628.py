# Generated by Django 3.0.6 on 2020-06-27 06:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_car_is_edited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
