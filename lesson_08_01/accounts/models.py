from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserFile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='')


class UserPhoto(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/%Y/%m/%d')

# user_photo = UserPhoto.objects.first()
# user = user_photo.user_id
