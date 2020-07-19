from django.contrib import admin

from .models import Event, EventType


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('user', 'type', 'title', 'description', 'start_time', 'notified')
    list_display = fields
    ordering = ['-start_time']


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = fields
