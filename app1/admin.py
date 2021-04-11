from django.contrib import admin

from .models import Pet
from .models import AdoptRequest

admin.site.register(Pet)
admin.site.register(AdoptRequest)
# Register your models here.
