# Generated by Django 4.2.4 on 2023-09-05 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('View_practice', '0004_service_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='title',
        ),
    ]
