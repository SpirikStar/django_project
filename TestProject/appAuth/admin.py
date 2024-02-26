from django.contrib import admin
from .models import ContentNews


@admin.register(ContentNews)
class ContentNewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'name_url']
    class Media:
        js = ('appAuth/js/point.js', )
