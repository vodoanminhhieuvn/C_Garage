from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from .models import Car, Car_Brand, HistoryTrackingCar, Accessories, RepairVote



@receiver(post_save, sender=Car)
def create_profile(sender, instance, created, **kwargs):
    if created:
        History = HistoryTrackingCar.objects.create(car_id=instance.car_id, user=instance.staff, action='AD')
        History.save()
        RepairVote.objects.create(car=instance)

        
@receiver(post_save, sender=Car)
def save_profile(sender, instance, **kwargs):
        instance.repairvote.save() 

