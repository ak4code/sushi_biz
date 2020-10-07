from django.urls import path
from .views import HomeIndexView, PageView, RobotsView

app_name = 'home'

urlpatterns = [
    path('<slug:slug>/', PageView.as_view(), name='page'),
    path('robots.txt', RobotsView.as_view(), name='robots'),
    path('', HomeIndexView.as_view(), name='index'),
]
