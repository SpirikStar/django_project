from django.contrib import admin
from .models import StaticLink

@admin.register(StaticLink)
class StaticLInkAdmin(admin.ModelAdmin):
    list_display = ['id', 'pub_news', 'os','type_device', 'date_time']
    list_display_links = ['pub_news', 'os','type_device', 'date_time']
    search_fields = ['pub_news']
    list_filter = ('date_time', )
    list_per_page = 20