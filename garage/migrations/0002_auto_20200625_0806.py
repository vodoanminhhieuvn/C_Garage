# Generated by Django 3.0.6 on 2020-06-25 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='data_received',
            new_name='date_received',
        ),
    ]