from django import forms
from blog.models.bloggerModel import Blogger
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UpdateBlogforms(forms.Form):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Your New Title"
            }
        ),
    )
    post_date = forms.DateField(
        required=True,
        widget=forms.SelectDateWidget(
            attrs={
            }
        ))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows': 5,
            'cols': 40,
            'class': "form-control",
            'placeholder': "Your New Description",
        }
    ))
    blogger = forms.ModelChoiceField(
        queryset=Blogger.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                'class': "form-select",
                'placeholder': "Assigned Blogger",
            }
        ))


class CreateBlogforms(forms.Form):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "Title"
            }
        ),
    )
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            'rows': 5,
            'cols': 40,
            'class': "form-control",
        }
    ))

    blogger = forms.ModelChoiceField(
        queryset=Blogger.objects.all(),
        required=True,
        widget=forms.Select(
            attrs={
                'class': "form-select",
            }
        ))
