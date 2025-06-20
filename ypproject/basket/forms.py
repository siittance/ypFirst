from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from shop.models import (
    ProductCategory, Magazine, Catalog,
    Order, PosOrder, Cart, Review, Promotion
)

class BasketAddProductForm(forms.Form):
    count = forms.IntegerField(
        min_value=1,
        initial=1,
        label='Количество',
    )
    reload = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderForm(forms.ModelForm):
    buyer_surname = forms.CharField(
        label='Фамилия',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
            'style': 'height: 2.75rem; box-sizing: border-box;'
        })
    )
    buyer_name = forms.CharField(
        label='Имя',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
            'style': 'height: 2.75rem; box-sizing: border-box;'
        })
    )
    buyer_middlename = forms.CharField(
        label='Отчество',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
            'style': 'height: 2.75rem; box-sizing: border-box;'
        })
    )
    comment = forms.CharField(
        label='Комментарий',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full p-2 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
            'style': 'height: 6rem; box-sizing: border-box;',
            'rows': 3
        })
    )
    delivery_address = forms.CharField(
        label='Адрес доставки',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
            'style': 'height: 2.75rem; box-sizing: border-box;'
        })
    )
    delivery_type = forms.ChoiceField(
        label='Тип доставки',
        choices=Order.TYPE_DELIVERY,
        widget=forms.Select(attrs={
            'class': 'w-full p-2 rounded-md bg-white text-black border border-orange-500 focus:border-orange-400 focus:ring focus:ring-orange-400 focus:ring-opacity-50',
            'style': 'height: 2.75rem; box-sizing: border-box;'
        })
    )

    class Meta:
        model = Order
        fields = [
            'buyer_surname',
            'buyer_name',
            'buyer_middlename',
            'comment',
            'delivery_address',
            'delivery_type'
        ]