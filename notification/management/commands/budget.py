from django.core.management import BaseCommand
from notification.models import T_Budget, T_Shop


class Command(BaseCommand):
    help = 'Command which run budget cli'

    def handle(self, *args, **options):
        print("in command")
