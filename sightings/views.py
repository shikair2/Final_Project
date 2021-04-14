  
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from sightings.models import Squirrel
from sightings.forms import AddNewForm,UpdateForm

from django.shortcuts import get_object_or_404

def index(request):
    squirrels = Squirrel.objects.all()

    context = {
            'squirrels': squirrels,
            }
    field_list = [field.name for field in Squirrel._meta.get_fields()]
    return render(request, "sightings/index.html", context)

def squirrel_details(request, Unique_Squirrel_ID):
    squirrel = get_object_or_404(Squirrel, pk=Unique_Squirrel_ID)

    context = {
        'squirrel': squirrel,
    }
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return HttpResponse('updated')
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return render(request, 'sightings/detail.html', context)

def add(request):
    if request.method == 'POST':
        form = AddNewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('You have added a new squirrel data.')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return render(request, 'sightings/add.html', {})

def stats(request):
    squirrels = Squirrel.objects.all()
    count = 0
    latitude = 0
    longitude = 0
    adult = 0
    juvenile = 0
    run_true = 0
    run_false = 0
    for squirrel in squirrels:
        count += 1
        latitude1 = getattr(squirrel, 'Latitude')
        latitude += latitude1
        longitude1 = getattr(squirrel, 'Longitude')
        longitude += longitude1
        age1 = getattr(squirrel, 'Age')
        if age1 == 'Adult':
            adult += 1
        elif age1 == 'Juvenile':
            juvenile += 1
        else:
            pass
        running1 = getattr(squirrel, 'Running')
        if running1 == True:
            run_true += 1
        elif running1 == False:
            run_false += 1
        else:
            pass
    
    latitude_avg = latitude/count
    longitude_avg = longitude/count
    context = {
            'count': count,
            'latitude_avg': latitude_avg,
            'longitude_avg': longitude_avg,
            'adult': adult,
            'juvenile': juvenile,
            'run_true': run_true,
            'run_false': run_false,
            }
    return render(request, "sightings/stats.html", context)

# Create your views here.
