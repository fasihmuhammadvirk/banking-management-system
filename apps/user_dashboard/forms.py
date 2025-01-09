from .models import MyUser
from django.forms import ModelForm


class UserLoginForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
