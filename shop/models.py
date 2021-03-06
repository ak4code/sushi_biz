from django.db import models
from django.urls import reverse
from easy_thumbnails.files import get_thumbnailer
from django.templatetags.static import static
from tinymce import HTMLField
from uuslug import uuslug
from home.models import HomeBase
from adminsortable.models import SortableMixin
from .managers import ProductManager, CategoryManager


class Category(SortableMixin, HomeBase):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = HTMLField(blank=True, null=True, verbose_name='Описание')
    active = models.BooleanField(default=True, verbose_name='Активная')
    is_promo = models.BooleanField(default=False, verbose_name='Участвует в акции')
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True, db_index=True, verbose_name='Ссылка')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name='Порядок')

    objects = CategoryManager()

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


class Product(SortableMixin, models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=255, verbose_name='Название')
    short_text = models.TextField(blank=True, null=True, verbose_name='Короткое описание')
    content = HTMLField(blank=True, null=True, verbose_name='Контент')
    image = models.ImageField(upload_to=product_image_path, blank=True, null=True, verbose_name='Картинка')
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='Цена')
    label = models.CharField(max_length=255, blank=True, null=True, verbose_name='Ярлык товара')
    active = models.BooleanField(default=True, verbose_name='Активный')
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True, verbose_name='Порядок')
    options = models.ManyToManyField('ProductOption', blank=True, verbose_name='Опции')

    objects = ProductManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('shop:product', args=[str(self.slug)])
        return 'url'

    def get_medium_img(self):
        if self.image:
            return get_thumbnailer(self.image)['medium'].url
        else:
            return static('shop/no-image.webp')

    def get_small_img(self):
        if self.image:
            return get_thumbnailer(self.image)['small'].url
        else:
            return static('shop/no-image.webp')

    class Meta:
        ordering = ['order']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductOption(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    value = models.CharField(max_length=255, verbose_name='Значение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Опция товара'
        verbose_name_plural = 'Опции товара'


class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя клиента')
    phone = models.CharField(max_length=255, verbose_name='Телефон клиента')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='Адрес клиента')
    person = models.PositiveIntegerField(default=1, verbose_name='Количество персон')
    delivery = models.BooleanField(default=False, verbose_name='Доставка')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'Заказ #{self.id}'

    @property
    def amount(self):
        return sum([item.amount for item in self.items.all()])

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    name = models.CharField(max_length=255, verbose_name='Наименование')
    product = models.ForeignKey('Product', blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Цена за шт.')

    @property
    def amount(self):
        return self.price * self.quantity

    @property
    def category_name(self):
        if self.product.category:
            return self.product.category.name
        else:
            return 'Без категории'

    @property
    def image(self):
        if self.product:
            return self.product.get_small_img()
        else:
            return static('shop/no-image.webp')

    def __str__(self):
        return f'{self.name} x {self.quantity} шт. = {self.amount} руб.'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
