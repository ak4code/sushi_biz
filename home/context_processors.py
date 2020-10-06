from django.core.cache import cache

from .models import Menu


def menu(request):
    cached_menus = cache.get('menus')
    if cached_menus is not None:
        return cached_menus
    menus = Menu.objects.prefetch_related('items')
    context = {'menu': {}}
    for menu in menus:
        context['menu'][menu.slug] = menu
    cache.set('menus', context, 300)
    return context
