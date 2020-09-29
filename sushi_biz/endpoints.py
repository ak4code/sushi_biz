from rest_framework import routers
from shop.views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
