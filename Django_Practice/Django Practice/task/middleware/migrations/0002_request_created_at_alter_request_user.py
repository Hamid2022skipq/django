# Generated by Django 4.1.4 on 2023-09-17 17:28

from django.conf import settings
from django.db import migrations, models
from django.utils import timezone
import django.db.models.deletion

def add_records(apps, schema_editor):
    Request = apps.get_model("middleware", "Request")
    Request.objects.create(user_id=1, view="hello world", visits=10, id=1, created_at=timezone.now())


def delete_records(apps, schema_editor):
    Request = apps.get_model("middleware", "Request")
    Request.objects.get(id=1).delete()


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('middleware', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.RunPython(add_records, delete_records),
        migrations.AlterField(
            model_name='request',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
