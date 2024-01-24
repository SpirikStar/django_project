from django.contrib import admin
from .models import ContentBanner, AboutMe, Documents


@admin.register(ContentBanner)
class ContentBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'desc', 'number']
    list_display_links = ['title', 'desc']
    ordering = ['number']

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['fio', 'desc', 'expert']
    list_display_links = ['fio', 'desc', 'expert']


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file']
    list_display_links = ['title', 'file']