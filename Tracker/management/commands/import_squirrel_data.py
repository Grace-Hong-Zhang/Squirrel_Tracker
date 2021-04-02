from django.core.management.base import BaseCommand
from Tracker.models import Squirrel
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file')

    def handle(self, *args, **options):
        unique_ids = []
        with open(options['file']) as file:
            # Squirrel.objects.all().delete()
            reader = csv.DictReader(file)
            for entry in reader:
                if entry['Unique Squirrel ID'] in unique_ids:
                    continue
                unique_ids.append(entry['Unique Squirrel ID'])
                Squirrel.objects.get_or_create(
                    x = float(entry['X']),
                    y = float(entry['Y']),
                    unique_squirrel_id = entry['Unique Squirrel ID'],
                    hectare = entry['Hectare'],
                    shift = entry['Shift'],
                    date = entry['Date'],
                    age = entry['Age'],
                    primary_fur_color = entry['Primary Fur Color'],
                    highlight_fur_color = entry['Highlight Fur Color'],
                    location = entry['Location'],
                    specific_location = entry['Specific Location'],
                    running = True if entry['Running'] == 'true' else False,
                    chasing = True if entry['Chasing'] == 'true' else False,
                    climbing = True if entry['Climbing'] == 'true' else False,
                    eating = True if entry['Eating'] == 'true' else False,
                    foraging = True if entry['Foraging'] == 'true' else False,
                    other_activities = entry['Other Activities'],
                    kuks = True if entry['Kuks'] == 'true' else False,
                    quaas = True if entry['Quaas'] == 'true' else False,
                    moans = True if entry['Moans'] == 'true' else False,
                    tail_flags = True if entry['Tail flags'] == 'true' else False,
                    tail_twitches = True if entry['Tail twitches'] == 'true' else False,
                    approaches = True if entry['Approaches'] == 'true' else False,
                    indifferent = True if entry['Indifferent'] == 'true' else False,
                    runs_from = True if entry['Runs from'] == 'true' else False,
                    other_interactions = entry['Other Interactions'],
                )