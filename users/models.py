from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
# Create your models here.

class UserProfileAdditional(models.Model):
   user = models.OneToOneField(User, on_delete = models.CASCADE)
   phone_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
   image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#This will overide the image file not creating new files in models
   def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
   
   def __str__(self):
    return f'{self.user.username}'

   def get_actions(self, request):
    actions = super().get_actions(request)
    if 'delete_selected' in actions:
        del actions['delete_selected']
    return actions


