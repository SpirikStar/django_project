from django.contrib import admin
from .models import GenerateNumber, GenerateDate


@admin.register(GenerateNumber)
class GenerateNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'status']
    list_display_links = ['number', ]
    list_filter = ['status', ]
    list_per_page = 10
    search_fields = ['number', ]
    ordering = ['-number']
    list_editable = ['status']


@admin.register(GenerateDate)
class GenerateDateAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time', 'status']
    list_display_links = ['date_time', ]
    list_filter = ['status', 'date_time']
    list_per_page = 10
    search_fields = ['date_time', ]
    readonly_fields = ['date_time']
    ordering = ['-date_time']
    list_editable = ['status']
    
