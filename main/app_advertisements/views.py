from django.shortcuts import render
from django.shortcuts import HttpResponse


def index(request):
    return render(request, 'index.html')

def earth(request):
    return render(request, 'earth.html')

def mars(request):
    return render(request, 'mars.html')

def venus(request):
    return render(request, 'venus.html')