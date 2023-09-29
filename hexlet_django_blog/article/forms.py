from django import forms
from django.forms import ModelForm
from .models import Article
from django.core import validators


class ArticleForm(ModelForm):
    name = forms.CharField(max_length=10, required=True)
    body = forms.CharField(max_length=10, required=True)

    class Meta:
        model = Article
        fields = ['name', 'body']
