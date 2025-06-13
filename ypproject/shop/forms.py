from django import forms
from .models import User, ProductCategory, Magazine, Catalog, Order, PosOrder, Cart, Review, Promotion

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_login', 'user_password', 'email', 'phone_number']
        widgets = {
            'user_password': forms.PasswordInput(),
        }

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name']

class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ['name_magazine', 'address_magazine']

class CatalogForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = [
            'product_name',
            'product_description',
            'product_price',
            'quantity',
            'product_category',
            'magazine',
            'image',
        ]
        widgets = {
            'product_description': forms.Textarea(attrs={'rows': 3}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_number', 'sum_bill', 'user']
        widgets = {
            'date_order': forms.DateTimeInput(attrs={'readonly': 'readonly'}),
        }

class PosOrderForm(forms.ModelForm):
    class Meta:
        model = PosOrder
        fields = ['catalog', 'order', 'count']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'catalog', 'quantity', 'price']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text', 'user', 'catalog']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 4}),
        }

class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['title', 'description', 'image', 'start_date', 'end_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }