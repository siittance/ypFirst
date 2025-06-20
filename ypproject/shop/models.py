from django.db import models
from django.contrib.auth.models import User



class ProductCategory(models.Model):
    category_name = models.CharField(max_length=25)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'
        ordering = ['category_name']

class Magazine(models.Model):
    name_magazine = models.CharField(max_length=25)
    address_magazine = models.CharField(max_length=60)

    def __str__(self):
        return self.name_magazine

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
        ordering = ['name_magazine']

class Catalog(models.Model):
    product_name = models.CharField(max_length=25)
    product_description = models.CharField(max_length=100, blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='catalog_images/')
    quantity = models.IntegerField()
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
        ordering = ['product_name']

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('completed', 'Завершен'),
        ('canceled', 'Отменен'),
    ]

    TYPE_DELIVERY = [
        ('pickup', 'Самовывоз'),
        ('courier', 'Курьер'),
        ('post', 'Почта'),
    ]

    delivery_type = models.CharField(max_length=10, choices=TYPE_DELIVERY, default='pickup')
    sum_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_order = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    buyer_surname = models.CharField(max_length=50, default='Неизвестно')
    buyer_name = models.CharField(max_length=50, null=True, blank=True)
    buyer_middlename = models.CharField(max_length=50, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    delivery_address = models.CharField(max_length=250, default='Неизвестно')

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date_order']

class PosOrder(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.catalog.product_name} x {self.count}"

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'
        ordering = ['order']

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.catalog} in cart"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        ordering = ['user']

class Review(models.Model):
    rating = models.IntegerField()
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review by {self.user} - {self.rating}/5"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

class Promotion(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='promotions/')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ['start_date']
