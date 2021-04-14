from django.forms import ModelForm

from .models import Squirrel


class AddNewForm(ModelForm):
    class Meta:
        model = Squirrel
        # All other fields are handled in the background
        fields = [
                             'Latitude', 
                            'Longitude',
                            'Unique_Squirrel_ID',
                            'Shift', 
                            'Date', 
                            'Age', 
                            'Primary_Fur_Color', 
                            'Location', 
                            'Specific_Location', 
                            'Running', 
                            'Chasing', 
                            'Climbing', 
                            'Eating',
                            'Foraging',           
                            'Other_Activities', 
                            'Kuks', 
                            'Quaas', 
                            'Moans', 
                            'Tail_Flags', 
                            'Tail_Twitches', 
                            'Approaches', 
                            'Indifferent', 
                            'Runs_From'
        ]

class UpdateForm(ModelForm):
    class Meta:
        model = Squirrel
        # All other fields are handled in the background
        fields = [
                             'Latitude',
                            'Longitude',
                            'Shift',
                            'Date',
                            'Age',
        ]
