from django.urls import path
from .views import HomeIndexView, PageView

app_name = 'home'

urlpatterns = [
    path('<slug:slug>/', PageView.as_view(), name='page'),
    path('', HomeIndexView.as_view(), name='index'),
]
