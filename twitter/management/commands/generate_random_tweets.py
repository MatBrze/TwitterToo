from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from faker.providers import internet, misc

from twitter import models

DEFAULT_USER_NUM = 3
DEFAULT_TWEET_PER_USER = 3


class Command(BaseCommand):
    help = 'Generates random tweets by random users'

    def handle(self, *args, **options):
        fake = Faker('pl_PL')
        fake.add_provider(internet)
        fake.add_provider(misc)

        for _ in range(DEFAULT_USER_NUM):
            user = User.objects.create_user(username=fake.name(),
                                            email=fake.email(),
                                            password=fake.password())
            for _ in range(DEFAULT_TWEET_PER_USER):
                tweet = models.Tweet(author=user,
                                     content=fake.text(
                                         max_nb_chars=
                                         models.TWITTER_MAXIMUM_TWEET_LENGTH))
                tweet.save()
