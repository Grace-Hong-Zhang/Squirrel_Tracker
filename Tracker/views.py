from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm

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

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('Tracker/sightings/')
    
    else:
        form = SquirrelForm()
        context = {'form': form}
    return render(request, 'Tracker/sightings/add.html')
    
def update(request,id):
    obj=get_object_or_404(Squirrel,unique_id=id)
    form=SquirrelForm(request.POST,instance=obj)
    context={'form':form}
    if form.is_valid():
        form.save()
        return redirect('Tracker/sightings/')
    else:
        return render(request,'Tracker/sightings/update.html',context)
