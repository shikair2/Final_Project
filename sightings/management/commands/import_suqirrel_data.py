from django.core.management.base import BaseCommand, CommandError
from sightings.models import Squirrel

import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv file', type=str)

    def handle(self, *args, **options):
        file_ = options['csv file']
        with open(file_) as fp :
            reader = csv.DictReader(fp)

            for dict_ in reader:
                obj = Squirrel()
                obj.Longitude=dict_['Y']
                obj.Latitude=dict_['X']
                obj.Unique_Squirrel_ID=dict_['Unique Squirrel ID']
                obj.Shift=dict_['Shift']
                obj.Date=dict_['Date'][4:]+'-'+dict_['Date'][:2]+'-'+dict_['Date'][2:4]
                obj.Age=dict_['Age']
                obj.Primary_Fur_Color=dict_['Primary Fur Color']
                obj.Location=dict_['Location']
                obj.Specific_Location=dict_['Specific Location']
                obj.Running=True if dict_['Running'].lower() == 'true' else False
                obj.Chasing=True if dict_['Chasing'].lower() == 'true' else False
                obj.Climbing=True if dict_['Climbing'].lower() == 'true' else False
                obj.Eating=True if dict_['Eating'].lower() == 'true' else False
                obj.Foraging=True if dict_['Foraging'].lower() == 'true' else False
                obj.Other_Activities=dict_['Other Activities']
                obj.Kuks=True if dict_['Kuks'].lower() == 'true' else False
                obj.Quaas=True if dict_['Quaas'].lower() == 'true' else False
                obj.Moans=True if dict_['Moans'].lower() == 'true' else False
                obj.Tail_Flags=True if dict_['Tail flags'].lower() == 'true' else False
                obj.Tail_Twitches=True if dict_['Tail twitches'].lower() == 'true' else False
                obj.Approaches=True if dict_['Approaches'].lower() == 'true' else False
                obj.Indifferent=True if dict_['Indifferent'].lower() == 'true' else False
                obj.Runs_From=True if dict_['Runs from'].lower() == 'true' else False
                obj.save()

            msg = 'You are importing data...'    
            self.stdout.write(
                    self.style.SUCCESS(msg)
                )
