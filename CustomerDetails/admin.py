from django.contrib import admin

from .models import adminassigment,userassigment


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(adminassigment)
class adminassigmentAdmin(admin.ModelAdmin):
    list_display = ['assigned_group']

@admin.register(userassigment)
class userassigmentAdmin(admin.ModelAdmin):
    list_display = ['user']


