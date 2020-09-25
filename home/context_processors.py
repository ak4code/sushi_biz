from .models import Menu


def menu(request):
    # cached_menus = cache.get(MYMENU_CACHE_KEY)
    # if cached_menus is not None:
    #     return cached_menus
    menus = Menu.objects.prefetch_related('items')
    context = {'menu': {}}
    for menu in menus:
        context['menu'][menu.slug] = menu
    # cache.set(MYMENU_CACHE_KEY, context, MYMENU_CACHE_TIMEOUT)
    return context
