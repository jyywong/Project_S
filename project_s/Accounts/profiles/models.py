from django.db import models
from django.conf import settings


class PI_Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='PI_profile', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.user.username) + ' profile'
class Grads_Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='Grads_profile', on_delete = models.CASCADE)

    def __str__(self):
        return str(self.user.username) + ' profile'
class Undergrad_Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='Undergrad_profile', on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.user.username) + ' profile'