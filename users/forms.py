from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","first_name","last_name",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email","first_name","last_name")


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields = ['email','first_name','last_name','password1','password2']
