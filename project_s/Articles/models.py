from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User
from project_s import settings
from ckeditor.fields import RichTextField


# Create your models here.
class Article (models.Model):
    name = models.CharField(max_length = 255)
    link = models.URLField()
    PI = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='article_PI')
    first_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='article_FA')
    article_text = RichTextField(blank = True, null=True)
    reviewers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reviewers')

    def __str__(self):
        truncated_name = Truncator(self.name)
        return truncated_name.chars(50)

    def save(self, *args, **kwargs):
        default_reviewers = [self.PI, self.first_author]
        self.add_reviewers(default_reviewers)
        super().save(*args, **kwargs)

    def add_reviewers(self, new_reviewers):
        for reviewer in new_reviewers:
            self.reviewers.add(reviewer)

        return self.reviewers
        


class Simple_article (models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='s_article')
    PI_verified = models.BooleanField(default = False)
    FA_verified = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    simple_text = RichTextField(blank = True, null=True)

    
class S_article_submission(models.Model):

    class submission_status(models.TextChoices):
        not_submitted = 'Awaiting submission', ('Awaiting submission')
        submitted = 'Submitted', ('Submitted')
        in_review = 'In Review', ('In Review')
        reviewed = 'Reviewed', ('Reviewed')


    article = models.ForeignKey(Article, on_delete= models.CASCADE, related_name='submission')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_this_submission')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=150, choices=submission_status.choices, default = submission_status.not_submitted)
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviewed_this_submission')
    text = RichTextField(blank=True, null=True)


    
