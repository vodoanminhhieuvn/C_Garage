from django.contrib import admin
from .models import Car, Car_Brand
from simple_history.admin import SimpleHistoryAdmin 


## Register Models
admin.site.register(Car_Brand)
admin.site.register(Car)

## Custom Admin Site
admin.site.site_header = 'C-Garage'
admin.site.site_title = 'C-Garage'
