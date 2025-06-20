from django import forms
from .models import ProductCategory, Magazine, Catalog, Order, PosOrder, Cart, Review, Promotion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


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

class RegistrationForm(UserCreationForm):
        username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
            'style': 'height: 2.75rem; box-sizing: border-box;'
        }),
             min_length=2
        )
        email = forms.CharField(
            label='Электронная почта',
            widget=forms.EmailInput(attrs={
                'class': 'w-full p-3 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
                'style': 'height: 2.75rem; box-sizing: border-box;'
            })
        )
        password1 = forms.CharField(
            label='Придумайте пароль',
            widget=forms.PasswordInput(attrs={
                'class': 'w-full p-3 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
                'style': 'height: 2.75rem; box-sizing: border-box;'
            })
        )
        password2 = forms.CharField(
            label='Повторите пароль',
            widget=forms.PasswordInput(attrs={
                'class': 'w-full p-3 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
                'style': 'height: 2.75rem; box-sizing: border-box;'
            })
        )

        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
        username = forms.CharField(
            label='Логин пользователя',
            widget=forms.TextInput(attrs={
                'class': 'w-full p-3 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
                'style': 'height: 2.75rem; box-sizing: border-box;'
            })
        )
        password = forms.CharField(
            label='Введите пароль',
            widget=forms.PasswordInput(attrs={
                'class': 'w-full p-3 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
                'style': 'height: 2.75rem; box-sizing: border-box;'
            })
        )


