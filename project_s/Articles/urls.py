from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name = 'Article_list')
]
