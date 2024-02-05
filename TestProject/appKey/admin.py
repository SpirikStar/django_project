from django.contrib import admin
from .models import Category, Product, Subcategory, PhotosProduct
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title',]
    list_display_links = ['title', ]
    list_filter = ['category', ]
    search_fields = ['title']


class SubcategoryStaked(admin.StackedInline):
    model = Subcategory  # Дочерний блок
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryStaked]

    class Meta:
        model = Category  # Родитель

class PhotosProductStaked(admin.StackedInline):
    model = PhotosProduct # Дочерний
    extra = 0

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    inlines = [PhotosProductStaked]
    list_display = ['id', 'subcategory', 'title', 'price']
    list_display_links = ['subcategory', 'title', ]
    raw_id_fields = ['subcategory', ]
    summernote_fields  = ('desc')
    class Meta:
        model = Product


