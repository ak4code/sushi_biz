from django.db import models


class MenuItemQuerySet(models.QuerySet):
    def active(self):
        return self.filter(show_in_menu=True)


class MenuItemManager(models.Manager):
    def get_queryset(self):
        return MenuItemQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()