from django.shortcuts import render, redirect
from Articles.models import Article, Simple_article, S_article_submission
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import Reviewer_Review_Form
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


def ReviewerView(request, pk):
    current_submission = S_article_submission.objects.get(id=pk)
    if request.user in current_submission.article.reviewers.all():
        is_reviewer = True
    if request.user in current_submission.article.approvers.all():
        is_approver = True

    if is_reviewer:
        query = Article.objects.filter(approvers=request.user)
        submissions = S_article_submission.objects.filter( Q(article__in=query) & ~Q(status = 'Awaiting submission'))
    elif is_approver:
        query = Article.objects.filter(reviewers=request.user)
        submissions = S_article_submission.objects.filter( Q(article__in=query) & ( Q(status = 'Submitted') | Q(status = 'In Review')))
    
    if current_submission not in submissions:
        return redirect('login')

    

    form = Reviewer_Review_Form(
        initial={
            'text' : current_submission.text
        }
    )
    if request.method == 'POST':
        form = Reviewer_Review_Form(request.POST)
        if request.POST.get('submit'):
            current_submission.status = 'Reviewed'
            current_submission.save()
            return redirect('reviewer_inbox')
        elif request.POST.get('approve'):
            current_submission.status = 'Approved'
            current_submission.save()
            return redirect('reviewer_inbox')
        elif request.POST.get('return_for_review'):
            current_submission.status = 'In Review'
            current_submission.save()
            return redirect('reviewer_inbox')
    else:
        form = Reviewer_Review_Form(
        initial={
            'text' : current_submission.text
        }
    )
    context = {
        'current' : current_submission,
        'form' : form,
        'submissions': submissions,
        'pk': pk,
        'is_reviewer' : is_reviewer,
        'is_approver' : is_approver
    }
    return render(request, 'reviewer_view2.html', context )

class ReviewerInboxArticles(ListView):
    model = Article
    paginate_by = 5
    context_object_name = 'articles'
    template_name = 'reviewer_inbox.html'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = Article.objects.filter(reviewers = user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Article.objects.filter(reviewers = self.request.user)
        submissions = S_article_submission.objects.filter( Q(article__in=query) & ( Q(status = 'Submitted') | Q(status = 'In Review')))
        context['submissions'] = submissions
        return context 


class SubmitterInbox(ListView):
    model = S_article_submission
    paginate_by = 5
    context_object_name = 'submissions'
    template_name = 'submitter_inbox.html'



    def post(self, request, *args, **kwargs):
        selected_submission = S_article_submission.objects.get(id = request.POST.get('id'))
        if request.POST.get('submit'):
            selected_submission.status = 'Submitted'
            selected_submission.save()
            return redirect('submitter_inbox')
        
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = S_article_submission.objects.filter(created_by = user)
        return queryset

class ApproverInbox(ListView):
    model = Article
    paginate_by = 5
    context_object_name = 'articles'
    template_name = 'approver_inbox.html'

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = Article.objects.filter(approvers = user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = Article.objects.filter(approvers = self.request.user)
        submissions = S_article_submission.objects.filter( Q(article__in=query) & Q(status='Reviewed'))
        context['submissions'] = submissions
        return context 