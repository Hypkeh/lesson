from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.TextField()
    until_date = models.DateTimeField()
    