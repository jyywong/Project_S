from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Simple_article, Article, S_article_submission
from .filters import ArticleFilter, SimpleArticleFilter
from django.db.models import Q
# Create your views here.
def home(request):
    template = 'index.html'
    context = {
        
    }
    return render (request, template, context)

class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    context_object_name = 'articles'
    template_name = 'article_list2.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter()
        return context 
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        myfilter = ArticleFilter(self.request.GET,  queryset = queryset)
        # myfilter.form.fields['name'] 

        filtered_queryset = myfilter.qs
        # Grab search bar data using request.POST.get, then combine that value with the filter form query
        # Use intersect function to combine the query from search bar and the filter form
        return filtered_queryset

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.kwargs.get('pk')
        return context 

class SimpleArticleListView(ListView):
    model = Simple_article
    paginate_by = 10
    context_object_name = 'articles'
    template_name = 'simple_article_list.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['filter'] = ArticleFilter()
        return context 
    
    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        myfilter = SimpleArticleFilter(self.request.GET,  queryset = queryset)
        filtered_queryset = myfilter.qs
        # Grab search bar data using request.POST.get, then combine that value with the filter form query
        # Use intersect function to combine the query from search bar and the filter form
        return filtered_queryset
class SimpleArticleSelectedView(DetailView):
    model = Article
    paginate_by = 5
    context_object_name = 'article'
    template_name = 'selected_simple_article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['simples'] = Simple_article.objects.filter(article__id = self.kwargs['pk'] )
        return context

class SimpleArticleDetailView(DetailView):
    model = Simple_article
    template_name = 'simple_article_detail.html'
    context_object_name = 'article'

class NewSimpleArticleSubmission(CreateView):
    model = S_article_submission
    fields = ['text']
    template_name = 'new_simple_article_submission.html'

class NewSimpleArticles(ListView):
    model = Simple_article
    template_name = 'new_simple_articles.html'
    context_object_name = 'new_simples'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = SimpleArticleFilter()
        return context 
    def get_queryset(self, *args, **kwargs):
        queryset = Simple_article.objects.order_by('-created_at')
        myfilter = SimpleArticleFilter(self.request.GET,  queryset = queryset)
        filtered_queryset = myfilter.qs
        # Grab search bar data using request.POST.get, then combine that value with the filter form query
        # Use intersect function to combine the query from search bar and the filter form
        return filtered_queryset