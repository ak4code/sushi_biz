import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from pprint import pprint


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.prefetch_related('products').filter(active=True)
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = category.products.all()
        page = self.paginate_queryset(products)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.active()
    serializer_class = ProductSerializer
    filterset_fields = ['category', ]


@csrf_exempt
def init_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        request.session['cart'] = data
        return JsonResponse({'success': True}, content_type='application/json', safe=False)
    try:
        cart = request.session['cart']
        return JsonResponse({'cart': cart})
    except KeyError:
        return JsonResponse({'cart': []})
