from django.core.management.base import BaseCommand
from Tracker.models import Squirrel
import pandas as pd

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        all_data = Squirrel.objects.all().values()
        df = pd.DataFrame(all_data)
        df.to_csv(options['file'], index=False)