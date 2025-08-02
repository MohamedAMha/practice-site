from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include("poll.urls")),  # handles base url of 127.0.0.1.8000
    path('poll/', include("poll.urls")),
    path('admin/', admin.site.urls),
]
