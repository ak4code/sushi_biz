from django.contrib import admin
from .models import Category, Product
from adminsortable2.admin import SortableAdminMixin


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('Основные', {
            'fields': ('name', 'description', 'active', 'is_promo')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'slug')
        }),
    )


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    fieldsets = (
        ('Основные', {
            'fields': ('name', 'category', 'short_text', 'price', 'image', 'content')
        }),
        ('Дополнительно', {
            'fields': ('active', 'label', 'order')
        }),
    )
