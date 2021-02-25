from adminsortable.admin import SortableAdmin
from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Category, Product, Order, OrderItem, ProductOption
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


def set_active(modeladmin, request, queryset):
    queryset.update(active=True)


set_active.short_description = "Сделать активными"


def set_inactive(modeladmin, request, queryset):
    queryset.update(active=False)


set_inactive.short_description = "Сделать неактивными"


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin, SortableAdmin):
    change_list_template_extends = 'admin/import_export/change_list_import_export.html'
    list_display = ('name', 'category', 'price', 'active')
    list_display_links = ('name',)
    list_filter = ('category', 'active')
    search_fields = ('name',)
    actions = [set_active, set_inactive, ]
    resource_class = ProductResource
    fieldsets = (
        ('Основные', {
            'fields': ('name', 'category', 'short_text', 'price', 'image', 'content', 'options')
        }),
        ('Дополнительно', {
            'fields': ('active', 'label',)
        }),
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('__str__', 'delivery', 'create_at', 'update_at')


@admin.register(ProductOption)
class ProductOption(admin.ModelAdmin):
    pass
