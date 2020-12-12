from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager
from Accounts.profiles.models import PI_Profile, Grads_Profile, Undergrad_Profile
from .profiles.models import PI_Profile, Grads_Profile, Undergrad_Profile
# Create your models here.

class User(AbstractUser):
    class UserType(models.TextChoices):
        PI = 'PI', ('Principal Investigator')
        Grads = 'Grads', ('Graduate Student')
        Undergrad = 'Undergrad', ('Undergrad')
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length = 150, choices = UserType.choices, default = UserType.Undergrad)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'type']
    # base_type = UserType.Undergrad
    objects = CustomUserManager()
    

    def save(self, *args, **kwargs):
        created = self.pk is None
        # if not self.pk:
        #     self.UserType = self.base_type
        super(User, self).save(*args, **kwargs)
        if created and self.type == 'PI':
            PI_Profile.objects.create(user = self)
        elif created and self.type == 'Grads':
            Grads_Profile.objects.create(user = self)
        elif created and self.type == 'Undergrad':
            Undergrad_Profile.objects.create(user = self)

class PI_Manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type = User.UserType.PI)

class PI(User):
    base_type = User.UserType.PI
    objects = PI_Manager()
    class Meta:
        proxy = True

    # Functions only available to PIs
    def extra(self):
        return self.PI_profile

class Grads_Manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type = User.UserType.PI)

class Grads(User):
    base_type = User.UserType.Grads
    objects = Grads_Manager()
    class Meta:
        proxy = True

    # Functions only available to Grads
    def extra(self):
        return self.Grads_profile

class Undergrad_Manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(type = User.UserType.Undergrad)

class Undergrad(User):
    base_type = User.UserType.Undergrad
    objects = Undergrad_Manager()
    class Meta:
        proxy = True

    # Functions only available to PIs
    def extra(self):
        return self.Undergrad_profile
