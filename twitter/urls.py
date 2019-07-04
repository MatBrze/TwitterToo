from django.urls import path
from twitter import views

app_name = 'twitter'

urlpatterns = [
    path('', views.MainWebPageView.as_view(), name="index"),
    path('compose/', views.TweetComposeView.as_view(), name="compose"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('tweet/<int:pk>/', views.TweetDetailView.as_view(),
         name='tweet-detail'),
    path('user/<int:pk>/', views.AuthorDetailView.as_view(),
         name='author-detail'),
    path('message/', views.MessageListView.as_view(), name='messages'),
    path('message/<int:pk>', views.MessageDetailView.as_view(),
         name='message-detail'),
    path('message/new/', views.ComposeMessageView.as_view(),
         name='compose-message'),
]