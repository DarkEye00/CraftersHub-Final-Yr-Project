from django import forms
from core.models import Product, Category


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Product Title",
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Category",
            }
        ),
    )

    image = forms.ImageField()

    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Price",
            }
        )
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Product Description",
            }
        )
    )
    specifications = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Product details/specifics ",
            }
        )
    )
    product_status = forms.ChoiceField(
        choices=Product.STATUS,
        required=True,
        widget=forms.Select(attrs={"class": "styled-choice-field"}),
    )

    class Meta:
        model = Product
        fields = [
            "title",
            "category",
            "image",
            "price",
            "description",
            "specifications",
            "product_status",
        ]
