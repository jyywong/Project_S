import django_filters
from django_filters import filters
from .models import *
from django import forms
class ArticleFilter(django_filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    class Meta:
        model = Article
        exclude = ['name', 'reviewers', 'approvers']


class SimpleArticleFilter(django_filters.FilterSet):
    article__name = filters.CharFilter(field_name="article__name", lookup_expr="icontains")
    class Meta:
        model = Simple_article
        fields = [
            'created_by', 
            'article__name',
            'article__PI',
            'article__first_author'
        ]
