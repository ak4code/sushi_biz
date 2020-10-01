from django.urls import path
from .views import CategoryDetailView

app_name = 'shop'

urlpatterns = [
    path('<slug:slug>/', CategoryDetailView.as_view(), name='category'),
]
