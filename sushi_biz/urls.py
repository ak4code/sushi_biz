"""sushi_biz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .endpoints import router as api
from shop.views import CartView, CheckoutView, init_cart

admin.site.site_header = 'Sushi-Shop'
admin.site.site_title = 'Sushi-Shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('menu/', include('shop.urls')),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/init/', init_cart, name='init-cart'),
    path('cart/checkout/', CheckoutView.as_view(), name='checkout'),
    path('api/', include(api.urls)),
    path('', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
