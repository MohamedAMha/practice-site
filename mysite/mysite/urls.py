from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/poll/')),
    path('poll/', include("poll.urls")),
    path('admin/', admin.site.urls),
]
