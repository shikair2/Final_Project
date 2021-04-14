from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sightings/', include('sightings.urls')),
    path('map/', include('map.urls')),
]
