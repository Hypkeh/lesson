# Generated by Django 5.0 on 2024-04-11 16:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0013_alter_ad_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7494fef0-d1c2-4187-b228-ee77a0558844'), editable=False, primary_key=True, serialize=False),
        ),
    ]
