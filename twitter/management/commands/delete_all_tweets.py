from django.core.management.base import BaseCommand

from twitter import models


class Command(BaseCommand):
    help = 'Deletes all tweets'

    def handle(self, *args, **options):
        models.Tweet.objects.all().delete()
