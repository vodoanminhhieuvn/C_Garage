# Generated by Django 3.0.7 on 2020-08-02 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0025_car_date_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='Fee',
            field=models.IntegerField(null=True),
        ),
    ]
