from django.db import models
from django.contrib.auth.models import User

TWITTER_MAXIMUM_TWEET_LENGTH = 280
TWITTER_MAXIMUM_COMMENT_LENGTH = 60
TWITTER_MAXIMUM_MSG_LENGTH = 64


class Tweet(models.Model):
    content = models.CharField(max_length=TWITTER_MAXIMUM_TWEET_LENGTH)
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '[{}] TWEET by {}: {}'.format(
            self.creation_date,
            self.author, self.content[:20])


class Comment(models.Model):
    content = models.CharField(max_length=TWITTER_MAXIMUM_COMMENT_LENGTH)
    date_comment = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Message(models.Model):
    title = models.CharField(max_length=TWITTER_MAXIMUM_MSG_LENGTH)
    content = models.TextField()
    date_send = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="user_from")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="user_to")
    read = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f'from: {self.sender} to: ' \
               f'{self.recipient} message: {self.content[0:20]}'
