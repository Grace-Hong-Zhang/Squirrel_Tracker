from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'Tracker/map.html', context)

def sightings(request):
    squirrels = Squirrel.objects.all()
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'Tracker/sightings.html', context)
