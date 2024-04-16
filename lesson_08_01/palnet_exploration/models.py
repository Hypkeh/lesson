from django.db import models

# Create your models here.


class Planet(models.Model):
    name = models.CharField(max_length=100)
    discovered_by = models.ForeignKey('Explorer', on_delete=models.CASCADE  )

    def __str__(self):
        return self.name


class Explorer(models.Model):
    name = models.CharField(max_length=100)
    expedition_date = models.DateField()

    def __str__(self):
        return self.name
