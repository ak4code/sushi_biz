# Generated by Django 3.1.1 on 2020-09-24 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('home', '0003_auto_20200925_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Тип контента'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID обьекта'),
        ),
    ]
