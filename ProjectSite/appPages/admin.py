from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'date']
    list_display_links = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title', 'content']
    ordering = ['-date']
