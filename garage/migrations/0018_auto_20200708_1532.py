# Generated by Django 3.0.6 on 2020-07-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0017_auto_20200708_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_id',
            field=models.CharField(editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]
