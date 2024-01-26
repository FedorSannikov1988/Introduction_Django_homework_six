from django import forms
from shop.models import Product


class EditProduct(forms.Form):

    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     empty_label='Выберите товар из списка',
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label='Товар:'
    )

    name = forms.CharField(min_length=1,
                           max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Введите новое название товара'}),
                               label='Новое название товара:'
    )

    description = forms.CharField(min_length=1,
                                  widget=forms.Textarea(
                                  attrs={'class': 'form-control'}),
                                  label='Описание товара:'
    )

    price = forms.FloatField(
                             widget=forms.NumberInput(
                             attrs={'class': 'form-control', 'min': 1}),
                             label='Новая цена:'
    )

    quantity = forms.IntegerField(
                             widget=forms.NumberInput(
                             attrs={'class': 'form-control', 'min': 1}),
                             label='Новое количество товара'
    )


class LoadImageForProduct(forms.Form):

    product = forms.ModelChoiceField(queryset=Product.objects.all(),
                                     empty_label='Выберите товар изображение для которого загружаете',
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label='Товар:'
    )

    #image = forms.ImageField(widget=forms.ClearableFileInput())
    image = forms.ImageField(widget=forms.FileInput())
    #image = forms.ImageField(widget=forms.TextInput())
    #image = forms.ImageField(widget=forms.URLInput())

