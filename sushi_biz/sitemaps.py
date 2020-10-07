from django.contrib import sitemaps
from django.urls import reverse

from home.models import Page
from shop.models import Category


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home:index', ]

    def location(self, item):
        return reverse(item)


class CategorySitemap(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Category.objects.active()

    def lastmod(self, obj):
        return obj.update_at


class PageSitemap(sitemaps.Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Page.objects.all()

    def lastmod(self, obj):
        return obj.update_at