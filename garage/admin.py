from django.contrib import admin
from .models import Car, Car_Brand
        
my_Models = [Car, Car_Brand]

admin.site.register(my_Models)
admin.site.site_header = 'C-Garage'
admin.site.site_title = 'C-Garage'