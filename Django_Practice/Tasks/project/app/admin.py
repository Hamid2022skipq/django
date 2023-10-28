from django.contrib import admin
from .models import *
@admin.register(React)
class ReactAdmin(admin.ModelAdmin):
    list_display = ('employee', 'department')