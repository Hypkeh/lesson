from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Author


@receiver(post_save, sender=Author)
def create_author(sender, **kwargs):
    if kwargs['created']:
        print('Создан новый автор')


@receiver(post_save)
def model_created(sender, **kwargs):
    print('Модель создана!')

