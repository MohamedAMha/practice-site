from django.urls import path
from . import views

app_name = "TWCSS"

urlpatterns = [
    path("TWCSS/tailwindcss", views.tailwindcss, name="tailwindcss"),
]