from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_display_links = ['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'category', 'price']
    list_display_links = ['title', 'category']
