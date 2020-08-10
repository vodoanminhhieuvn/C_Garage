from django.contrib import admin
from .models import Car, Car_Brand, HistoryTrackingCar, Accessories, RepairVote
from simple_history.admin import SimpleHistoryAdmin 

my_Models = [Car, Car_Brand, HistoryTrackingCar, Accessories, RepairVote]
## Register Models
admin.site.register(my_Models)

## Custom Admin Site
admin.site.site_header = 'C-Garage'
admin.site.site_title = 'C-Garage'
