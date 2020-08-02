from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from simple_history.models import HistoricalRecords
# Create your models here.

class Car_Brand(models.Model):
    car_code = models.CharField(primary_key=True, max_length=100)
    car_name = models.CharField(max_length=200)
    history = HistoricalRecords(inherit=True)
    def __str__(self):
        return self.car_name

class Car(models.Model):
    car_id = models.CharField(primary_key=True, max_length=100)
    owner = models.CharField(max_length=200)
    license_plate = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    email = models.EmailField()
    date_received = models.DateTimeField(default=timezone.now)
    date_finished = models.DateTimeField(null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    car_brand = models.ForeignKey('Car_brand', on_delete=models.CASCADE)
    fee = models.IntegerField(null=True)
    is_edited = models.BooleanField(default=False, null=True)
    status = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        if not self.car_id:
            self.car_id = self.car_brand.car_code + self.phone_number
        super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return self.car_id
    
    def get_absolute_url(self):
        return reverse('garage-home')

