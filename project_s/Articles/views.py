from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Simple_article, Article, S_article_submission
from .filters import ArticleFilter
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
    template_name = 'article_list.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ArticleFilter()
        return context 
    
    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get('q')
        
        if not query:
            queryset = super().get_queryset(*args, **kwargs)
        else:
            queryset = Article.objects.filter(Q(name__icontains = query))
        myfilter = ArticleFilter(self.request.GET, queryset = queryset)
        filtered_queryset = myfilter.qs

        # Use intersect function to combine the query from search bar and the filter form
        return filtered_queryset

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_article = Article.objects.get(id = self.kwargs['pk'])
        corresponding_simple = Simple_article.objects.get(article = current_article)
        context['simple'] = corresponding_simple.id
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
        query = self.request.GET.get('q')
        
        if not query:
            queryset = super().get_queryset(*args, **kwargs)
        else:
            queryset = Simple_article.objects.filter(Q(name__icontains = query))
        # myfilter = ArticleFilter(self.request.GET, queryset = queryset)
        # filtered_queryset = myfilter.qs

        # Use intersect function to combine the query from search bar and the filter form
        return queryset

class SimpleArticleDetailView(DetailView):
    model = Simple_article
    template_name = 'simple_article_detail.html'
    context_object_name = 'article'

class NewSimpleArticleSubmission(CreateView):
    model = S_article_submission
    fields = ['text']
    template_name = 'new_simple_article_submission.html'