from rest_framework.serializers import ModelSerializer, CharField
from .models import Product, Category


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
