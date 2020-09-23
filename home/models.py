from django.db import models
from solo.models import SingletonModel
from tinymce import HTMLField
from uuslug import uuslug


class HomeBase(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    seo_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='SEO заголовок')
    seo_description = models.TextField(max_length=255, blank=True, null=True, verbose_name='SEO описание')

    class Meta:
        abstract = True


class HomeConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Интернет магазин', verbose_name='Название сайта')
    maintenance_mode = models.BooleanField(default=False, verbose_name='Режим обслуживания')
    home_page = models.OneToOneField('Page', on_delete=models.CASCADE, verbose_name='Главная страница')

    def __str__(self):
        return "Настройки"

    class Meta:
        verbose_name = "Настройки"


class Page(HomeBase):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = HTMLField(blank=True, null=True, verbose_name='Контент')
    slug = models.SlugField(max_length=255, blank=True, null=True, verbose_name='ЧПУ ссылка')

    def get_seo_title(self):
        return self.seo_title or self.title

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuslug(self.title, instance=self)
        super(Page, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='Ссылка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class MenuItem(models.Model):
    LINK_TARGET_CHOICES = (
        ('_blank', '_blank'),
        ('_top', '_top'),
        ('_parent', '_parent'),
    )
    menu = models.ForeignKey('Menu', related_name='items', on_delete=models.CASCADE, verbose_name='Меню')
    name = models.CharField(max_length=255, verbose_name='Название')
    link = models.CharField(max_length=255, verbose_name='Произвольная ссылка')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Аттрибут title=')
    target = models.CharField(
        max_length=10,
        choices=LINK_TARGET_CHOICES,
        null=True,
        blank=True,
        verbose_name='Аттрибут target='
    )
    show_in_menu = models.BooleanField(default=True, verbose_name='Отображать в меню')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.name
        super(MenuItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"