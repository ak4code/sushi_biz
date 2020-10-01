from rest_framework.serializers import ModelSerializer, CharField
from .models import Product, Category, Order, OrderItem


class ProductSerializer(ModelSerializer):
    url = CharField(read_only=True, source='get_absolute_url')
    small_img = CharField(read_only=True, source='get_small_img')
    medium_img = CharField(read_only=True, source='get_medium_img')

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'name', 'product', 'quantity', 'price', 'amount', 'image']
        read_only_fields = ['amount', 'image']


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items:
            OrderItem.objects.create(order=order, **item)
        return order
