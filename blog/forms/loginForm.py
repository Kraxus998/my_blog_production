from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django import forms


class MyLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': "form-control", 'placeholder': "Username"}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'class': "form-control", 'placeholder': "Password"}),
    )


class MyRegisterForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': "form-control", 'placeholder': "Username"}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", 'class': "form-control", 'placeholder': "Password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", 'class': "form-control", 'placeholder': "Password  Confirmation"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
