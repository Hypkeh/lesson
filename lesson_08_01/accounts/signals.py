from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.core.signing import Signer


@receiver(post_save, sender=User)
def send_activation_mail(sender, instance, created, **kwargs):
    if created:
        signer = Signer()

        signed_username = signer.sign(instance.username)

        activation_link = f"http:/127.0.0.1:8000/{reverse_lazy('user_activate', kwargs={'signed_username': signed_username})}"

        instance.is_active = False
        instance.save()

        email = EmailMessage('Ссылка для активации',
                             f'Ваша ссылка для активации: {activation_link}',
                             'admin@mysite.com',
                             to=[instance.email])
        email.send()

