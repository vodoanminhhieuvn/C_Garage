from django.contrib import admin
from .models import UserProfileAdditional
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(UserProfileAdditional)
admin.site.unregister(Group)
admin.site.disable_action('delete_selected')