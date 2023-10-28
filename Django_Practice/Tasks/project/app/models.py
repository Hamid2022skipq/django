from django.db import models

# Create your models here.


class React (models.Model):
    employee = models.CharField(max_length=200)
    department = models.TextField()
