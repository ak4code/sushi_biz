from django.views.generic import DetailView
from .models import Category


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
