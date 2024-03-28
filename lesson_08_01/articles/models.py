from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Photo(models.Model):
    title = models.CharField(max_length=100)


class Comment(models.Model):
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Spare(models.Model):
    name = models.CharField(max_length=40)


class Machine(models.Model):
    name = models.CharField(max_length=40)
    spares = models.ManyToManyField(Spare, through='Kit', through_fields=('machine_id', 'spare_id'))


class Kit(models.Model):
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare_id = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField()


class Car(Machine):
    max_speed = models.IntegerField()


class AssemblyLine(Machine):
    max_capacity = models.IntegerField()
