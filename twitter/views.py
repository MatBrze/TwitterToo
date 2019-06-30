from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django import views
from django.urls import reverse_lazy

from twitter import models
from django.views.generic import CreateView
from twitter import forms
from .forms import UserRegisterForm
# Create your views here.


class MainWebPageView(views.View):

    def get(self, request):
        tweets = models.Tweet.objects.order_by('-creation_date').all()
        ctx = {
            'tweets': tweets
        }
        return render(request, 'twitter/index.html', ctx)


class TweetComposeView(LoginRequiredMixin, CreateView):
    model = models.Tweet
    form_class = forms.TweetForm
    success_url = reverse_lazy('twitter:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RegisterView(views.View):

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'twitter/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'{user} Konto zostało utworzone! Zaloguj się')
            return redirect('twitter:login')
        return render(request, 'twitter/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, views.View):

    def get(self, request):
        tweets = models.Tweet.objects.filter(
            author=request.user).order_by('-creation_date')
        return render(request, 'twitter/profile.html', {'tweets': tweets})


class TweetDetailView(views.View):

    def get(self, request, pk):
        tweet = models.Tweet.objects.get(pk=pk)
        add_comment = forms.AddCommentForm()
        return render(request, 'twitter/tweet_detail.html',
                      {'tweet': tweet, 'add_comment': add_comment})

    def post(self, request, pk):
        form = forms.AddCommentForm(request.POST)
        tweet = models.Tweet.objects.get(pk=pk)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            new_comment = models.Comment(
                content=content, author=request.user, tweet=tweet)
            new_comment.save()
            form = forms.AddCommentForm()
        return render(request, 'twitter/tweet_detail.html',
                      {'tweet': tweet, 'add_comment': form})
