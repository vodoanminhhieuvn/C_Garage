# Generated by Django 3.0.6 on 2020-07-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0005_auto_20200627_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='is_edited',
            field=models.BooleanField(null=True),
        ),
    ]
