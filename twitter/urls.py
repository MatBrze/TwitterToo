from django.urls import path
from django.contrib.auth import views as auth_views

from twitter import views
app_name = 'twitter'

urlpatterns = [
    path('', views.MainWebPageView.as_view(), name="index"),
    path('compose/', views.TweetComposeView.as_view(), name="compose"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]