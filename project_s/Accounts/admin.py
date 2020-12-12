from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .profiles.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(PI_Profile)
admin.site.register(Grads_Profile)
admin.site.register(Undergrad_Profile)
