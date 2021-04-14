from django.shortcuts import render
from sightings.models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'squirrels': squirrels,
            }

    return render(request, "map/index.html", context)
# Create your views here.
