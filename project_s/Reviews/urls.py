from django.urls import path
from . import views 
urlpatterns = [
    path('<int:pk>', views.ReviewerView, name='reviewing page'),
    path('inbox', views.ReviewerInboxArticles.as_view(), name='reviewer_inbox'),
    path('my_submissions', views.SubmitterInbox.as_view(), name='submitter_inbox')
]