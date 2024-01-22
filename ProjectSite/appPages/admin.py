from django.contrib import admin
from .models import ContentBanner


@admin.register(ContentBanner)
class ContentBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'number']
    list_display_links = ['title', 'desc']
    ordering = ['number']