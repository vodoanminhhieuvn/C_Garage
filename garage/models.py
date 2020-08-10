from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.admin.models import LogEntry
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Car_Brand(models.Model):
    car_code = models.CharField(primary_key=True, max_length=100)
    car_name = models.CharField(max_length=200)

    def __str__(self):
        return self.car_name

class Car(models.Model):

    STATUS_CHOICE = (
        (True, "Active"),
        (False, "UnActive")
    )

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
    status = models.BooleanField(default=True, null=True, choices=STATUS_CHOICE)
    
    def save(self, *args, **kwargs):
        if not self.car_id:
            self.car_id = self.car_brand.car_code + self.phone_number
        super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return self.car_id
    
    def get_absolute_url(self):
        return reverse('garage-home')

class HistoryTrackingCar(models.Model):

    class ActionType(models.TextChoices):
        ADD = 'AD', _('Add')
        DELETE = 'DE', _('Delete')
        EDIT = 'ED', _('Edit')

    action = models.CharField(max_length=2, choices=ActionType.choices)
    action_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.CharField(max_length=100, null=True)
   
    def __str__(self):
        return self.user.username


class Accessories(models.Model):
    accessories_name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.accessories_name

class RepairVote(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car.car_id
