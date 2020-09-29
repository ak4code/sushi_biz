from django.urls import path
from .views import CategoryDetailView, init_cart

app_name = 'shop'

urlpatterns = [
    path('init-cart/', init_cart, name='init-cart'),
    path('<slug:slug>/', CategoryDetailView.as_view(), name='category'),
]
