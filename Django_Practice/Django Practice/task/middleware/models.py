from django.db import models
from django.contrib.auth.models import User
class Request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="requests")
    view = models.CharField(max_length=250) # this could also represent a URL
    visits = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True, null=True)