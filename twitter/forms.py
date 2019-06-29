from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from twitter import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TweetForm(forms.ModelForm):
    class Meta:
        model = models.Tweet
        fields = ['content']
        widgets = {
            'content': forms.Textarea()
        }