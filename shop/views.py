import json

from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, TemplateView
from rest_framework import permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Category, Product, Order
from .serializers import ProductSerializer, CategorySerializer, OrderSerializer
from .permissions import IsClient
from .utils import order_create_notification


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.prefetch_related('products').filter(active=True)
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = category.products.active()
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


class CartView(TemplateView):
    template_name = 'shop/cart.html'

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart')
        if not cart:
            return HttpResponseRedirect('/')
        return super(CartView, self).get(request, *args, **kwargs)


class CheckoutView(TemplateView):
    template_name = 'shop/checkout.html'
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['client'] = request.POST.get('client')
        return self.render_to_response(context)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.prefetch_related('items')
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$phone']

    def get_permissions(self):
        """
        Определяет вьюху и применяет к ней права доступа.
        """
        if self.action == 'create':
            permission_classes = [IsClient]
        else:
            permission_classes = [permissions.DjangoModelPermissions]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        order_create_notification(serializer.save())