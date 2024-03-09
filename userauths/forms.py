from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
from core.models import Vendor
from django.core.validators import EmailValidator


class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Username",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Email Address",
            }
        )
    )
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "styled-choice-field"}),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Password",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Confirm Password",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]


class VendorProfileForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "Title eg Mr, Mrs, Ms, Dr",
            }
        )
    )
    image = forms.ImageField()
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "say something about yourself",
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "example: Luthuli ave, Nairobi",
            }
        )
    )
    contact = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "style": "padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;",
                "placeholder": "xxx-(xxxx)-xxx",
            }
        )
    )

    class Meta:
        model = Vendor
        fields = [
            "title",
            "image",
            "description",
            "address",
            "contact",
        ]
