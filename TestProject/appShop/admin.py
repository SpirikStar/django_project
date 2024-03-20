from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import ProductShop


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
    list_per_page = 20

@admin.register(ProductShop)
class ProductShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'count', 'price']
    list_display_links = ['title', 'count']
    list_per_page = 20
