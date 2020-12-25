import django_filters
from django_filters import filters
from .models import *
from django import forms
class ArticleFilter(django_filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains", widget = forms.HiddenInput())
    class Meta:
        model = Article
        exclude = ['name', 'reviewers', 'approvers']



