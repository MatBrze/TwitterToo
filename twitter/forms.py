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


class AddCommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'cols': 80}),
        max_length=models.TWITTER_MAXIMUM_COMMENT_LENGTH,
        label='')

    class Meta:
        model = models.Comment
        fields = ['content']
        labels = False


class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['title', 'content', 'recipient']
        widgets = {
            'content': forms.Textarea()
        }
