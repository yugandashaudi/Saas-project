from django.contrib import admin

from .models import Adminassigment,Userassigment


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(Adminassigment)
class AdminassigmentAdmin(admin.ModelAdmin):
    list_display = ['assigned_group']

@admin.register(Userassigment)
class UserassigmentAdmin(admin.ModelAdmin):
    list_display = ['user']


