from django.contrib import admin
from genericadmin.admin import GenericAdminModelAdmin, TabularInlineWithGeneric
from adminsortable.admin import SortableAdmin, SortableTabularInline

from .models import HomeConfiguration, Page, Menu, MenuItem
from solo.admin import SingletonModelAdmin


@admin.register(HomeConfiguration)
class HomeConfigurationAdmin(SingletonModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_absolute_url', 'create_at', 'update_at')
    fieldsets = (
        ('Основные', {
            'fields': ('title', 'content')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'slug')
        }),
    )


class MenuItemsInline(SortableTabularInline, TabularInlineWithGeneric):
    model = MenuItem
    extra = 0
    exclude = ('title', 'target')


@admin.register(Menu)
class MenuAdmin(GenericAdminModelAdmin, SortableAdmin):
    inlines = [MenuItemsInline, ]
    content_type_whitelist = ('home/page', 'shop/category')


@admin.register(MenuItem)
class MenuItemAdmin(SortableAdmin, GenericAdminModelAdmin):
    content_type_whitelist = ('home/page', 'shop/category')
    list_filter = ('menu',)
