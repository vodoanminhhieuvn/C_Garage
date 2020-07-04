from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

class Car_Brand(models.Model):
    car_code = models.CharField(primary_key=True, max_length=100)
    car_name = models.CharField(max_length=200)
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
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    car_code = models.ForeignKey('Car_brand', on_delete=models.CASCADE)
    is_edited = models.BooleanField()
    def __str__(self):
        return self.owner

