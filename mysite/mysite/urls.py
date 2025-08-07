from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("poll.urls")),  # handles base url of 127.0.0.1.8000
    # gonna want index to include a link to TWCSS' index page
    path('poll/', include("poll.urls")),
    path('twcss/', include('TWCSS.urls', namespace='TWCSS')),
    path('admin/', admin.site.urls),
]
