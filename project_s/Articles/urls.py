from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name = 'Article_list'),
    path('simple', views.SimpleArticleListView.as_view(), name = 'Simple_article_list'),
    path('<int:pk>', views.ArticleDetailView.as_view(), name='Article_detail'),
    path('simple/<int:pk>', views.SimpleArticleDetailView.as_view(), name = 'Simple_article_detail'),
    path('new_submission', views.NewSimpleArticleSubmission.as_view(), name='New_submission')
]
