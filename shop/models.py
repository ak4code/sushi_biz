from django.db import models
from django.urls import reverse
from tinymce import HTMLField
from uuslug import uuslug
from home.models import HomeBase


class Category(HomeBase):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = HTMLField(blank=True, null=True, verbose_name='Описание')
    active = models.BooleanField(default=True, verbose_name='Активная')
    is_promo = models.BooleanField(default=False, verbose_name='Участвует в акции')
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True, db_index=True, verbose_name='Ссылка')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')

    def get_absolute_url(self):
        return reverse('shop:category', args=[str(self.slug)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.name, instance=self)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-order']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


def product_image_path(instance, filename):
    category = instance.category.slug or 'empty'
    return f'catalog/products/{category}/{filename}'


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Название')
    short_text = models.TextField(blank=True, null=True, verbose_name='Короткое описание')
    content = HTMLField(blank=True, null=True, verbose_name='Контент')
    image = models.ImageField(upload_to=product_image_path, blank=True, null=True, verbose_name='Картинка')
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='Цена')
    label = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ярлык товара')
    active = models.BooleanField(default=True, verbose_name='Активный')
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Порядок')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
