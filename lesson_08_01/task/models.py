from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    CHOICES = (
        ('t', 'Преподаватель'),
        ('s', 'Студент')
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile_type = models.CharField(max_length=1, choices=CHOICES)


class Course(models.Model):
    title = models.CharField(max_length=50)
    teacher_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
