from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Simple_article
# Create your views here.
def home(request):
    template = 'index.html'
    context = {
        
    }
    return render (request, template, context)

class ArticleListView(ListView):
    model = Simple_article
    paginate_by = 10
    template_name = 'article_list.html'
   
        