# Generated by Django 5.2.2 on 2025-06-16 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ['user'], 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины'},
        ),
        migrations.AlterModelOptions(
            name='catalog',
            options={'ordering': ['product_name'], 'verbose_name': 'Каталог', 'verbose_name_plural': 'Каталоги'},
        ),
        migrations.AlterModelOptions(
            name='magazine',
            options={'ordering': ['name_magazine'], 'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date_order'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='posorder',
            options={'ordering': ['order'], 'verbose_name': 'Позиция заказа', 'verbose_name_plural': 'Позиции заказа'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ['category_name'], 'verbose_name': 'Категория продукта', 'verbose_name_plural': 'Категории продуктов'},
        ),
        migrations.AlterModelOptions(
            name='promotion',
            options={'ordering': ['start_date'], 'verbose_name': 'Акция', 'verbose_name_plural': 'Акции'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_at'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['user_login'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
