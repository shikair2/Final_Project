from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .forms import RequestForm
from .models import Pet

def index(request):
    pets = Pet.objects.all()
    context = {
            'pets':pets,
    }
    return render(request, 'app1/index.html', context)

def detail(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)

    context = {
            'pet':pet,
    }
    return render(request, 'app1/detail.html', context)

def adopt_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
   
    return JsonResponse({}, status=405)
# Create your views here.
