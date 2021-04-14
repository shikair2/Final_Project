from django.forms import ModelForm

from .models import AdoptRequest

class RequestForm(ModelForm):
    class Meta:
        model = AdoptRequest
        fields = [
                'pet',
                'adopter',
        ]
