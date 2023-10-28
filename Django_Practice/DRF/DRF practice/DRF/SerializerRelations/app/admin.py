from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id','name','gander']


@admin.register(Song)
class NameAdmin(admin.ModelAdmin):
    list_display = ['id','title','singer','duration']



