# Generated by Django 3.0.7 on 2020-08-09 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0037_repairvote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repairvote',
            old_name='car_id',
            new_name='car',
        ),
    ]