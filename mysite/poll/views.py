from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Dis da index payge. oh yeah, oh yeah, wee woo we woo")
