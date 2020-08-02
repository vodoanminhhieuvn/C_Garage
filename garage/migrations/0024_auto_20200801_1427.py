# Generated by Django 3.0.7 on 2020-08-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0023_auto_20200801_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_edited',
            field=models.BooleanField(default=False, null=True),
        ),
    ]