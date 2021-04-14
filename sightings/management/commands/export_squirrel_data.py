import csv
  
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
                                                          
class Command(BaseCommand):                                                         
    help = ("Exporting data to .csv")
                                                          
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
                                                          
    def handle(self, *args, **options):
        file_=options['csv_file']

        field_list = [f.name for f in Squirrel._meta.get_fields()]
        attr_list = ['Latitude', 'Longitude', 'Unique_Squirrel_ID', 'Shift', 'Date', 'Age', 'Primary_Fur_Color', 'Location', 'Specific_Location', 'Running', 'Chasing', 'Climbing', 'Eating', 'Foraging', 'Other_Activities', 'Kuks', 'Quaas', 'Moans', 'Tail_Flags', 'Tail_Twitches', 'Approaches', 'Indifferent', 'Runs_From']
        with open(file_, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(field_list)

            squirrels = Squirrel.objects.all()
                                                          
            for obj in squirrels:
                value_list = [getattr(obj, f) for f in attr_list]
                writer.writerow(value_list)
        csvfile.close()
