from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User

class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={"style":"padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;", "placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"style":"padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;", "placeholder":"Email Address"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"style":"padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;", "placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"style":"padding:10px; border-width:1px; border-color:gray; width:250px; border-radius:7px;", "placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ['username', 'email']