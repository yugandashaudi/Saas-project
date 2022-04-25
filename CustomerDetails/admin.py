from django.contrib import admin

from .models import Details,Myalert,Worksubmit

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['Name']

@admin.register(Myalert)
class MyalertAdmin(admin.ModelAdmin):
    list_display = ['Description']

@admin.register(Worksubmit)
class WorksubmitAdmin(admin.ModelAdmin):
    list_display = ['Name']

