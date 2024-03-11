from django.contrib import admin
from .models import PubNews

@admin.register(PubNews)
class PubNewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_url', 'date_time', 'count']
    list_display_links = ['name_url', 'date_time']
    ordering = ['date_time']