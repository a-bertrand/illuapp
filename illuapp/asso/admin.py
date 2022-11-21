from django.contrib import admin
from .models import AssoUser, Event, Table

@admin.register(AssoUser)
class AssoUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass