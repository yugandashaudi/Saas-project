from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_tenants.admin import TenantAdminMixin

from .models import Adminassigment,Userassigment



class AdminassigmentAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['assigned_group']

class UserassigmentAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Adminassigment, AdminassigmentAdmin)
admin.site.register(Userassigment, UserassigmentAdmin)


