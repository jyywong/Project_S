from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User
from project_s import settings

# Create your models here.
class Article (models.Model):
    name = models.CharField(max_length = 100)
    link = models.URLField()
    PI = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='article_PI')
    first_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='article_FA')
    article_text = models.TextField()

    def __str__(self):
        truncated_name = Truncator(self.name)
        return truncated_name.chars(50)

class Simple_article (Article):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='s_article')
    PI_verified = models.BooleanField(default = False)
    FA_verified = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    simple_text = models.TextField()

    
    



    
