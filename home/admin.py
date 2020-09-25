from django.contrib import admin
from genericadmin.admin import GenericAdminModelAdmin, TabularInlineWithGeneric, StackedInlineWithGeneric

from .models import HomeConfiguration, Page, Menu, MenuItem
from solo.admin import SingletonModelAdmin


@admin.register(HomeConfiguration)
class HomeConfigurationAdmin(SingletonModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'create_at', 'update_at')
    fieldsets = (
        ('Основные', {
            'fields': ('title', 'content')
        }),
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'slug')
        }),
    )


class MenuItemsInline(TabularInlineWithGeneric):
    model = MenuItem
    extra = 1
    exclude = ('title', 'target')


@admin.register(Menu)
class MenuAdmin(GenericAdminModelAdmin):
    inlines = [MenuItemsInline, ]
    content_type_whitelist = ('home/page', 'shop/category')


@admin.register(MenuItem)
class MenuItemAdmin(GenericAdminModelAdmin):
    content_type_whitelist = ('home/page', 'shop/category')
