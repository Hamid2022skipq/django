# Generated by Django 4.2.6 on 2023-10-17 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='react',
            name='department',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='react',
            name='employee',
            field=models.CharField(max_length=200),
        ),
    ]
