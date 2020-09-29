from adminsortable.admin import SortableAdmin
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Category, Product
from import_export import resources


@admin.register(Category)
class CategoryAdmin(SortableAdmin):
    fieldsets = (
        ('Основные', {
            'fields': ('name', 'description', 'active', 'is_promo')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'slug')
        }),
    )


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin, SortableAdmin):
    change_list_template_extends = 'admin/import_export/change_list_import_export.html'
    list_display = ('name', 'category', 'price', 'active')
    list_display_links = ('name',)
    list_filter = ('category', 'active')
    search_fields = ('title',)
    resource_class = ProductResource
    fieldsets = (
        ('Основные', {
            'fields': ('name', 'category', 'short_text', 'price', 'image', 'content')
        }),
        ('Дополнительно', {
            'fields': ('active', 'label',)
        }),
    )
