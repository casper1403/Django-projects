from django.db import models
from PIL import Image
# import the user model
from django.contrib.auth.models import User
# Create your models here.
# extend the user model
# user can have profile pictures
# Register model in admin

# Model for user class
class Profile(models.Model):
    # Declare that this model had a one to one relation ship with the existing user model and gets deleted on delete
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


    # Resize images uploaded to you model.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
