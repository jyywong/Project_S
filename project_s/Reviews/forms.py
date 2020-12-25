from django.forms import ModelForm
from project_s import settings
from django.contrib.auth import get_user_model
from django import forms
from Articles.models import S_article_submission
from ckeditor.widgets import CKEditorWidget

class Reviewer_Review_Form(ModelForm):

    comments = forms.CharField(widget = forms.Textarea, required = False)
    text = forms.CharField(widget = CKEditorWidget())

    class Meta:
        model = S_article_submission
        fields = ['text', 'created_by']

    