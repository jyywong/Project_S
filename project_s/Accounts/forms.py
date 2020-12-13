from django.forms import ModelForm
from project_s import settings
from django.contrib.auth import get_user_model
class SignUpForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'email',
            'type'
        ]