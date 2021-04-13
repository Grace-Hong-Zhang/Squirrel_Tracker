from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirrelForm

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
        'squirrels': squirrels,
    }
    return render(request, 'sightings/map.html', context)

def sightings(request):
    squirrels = Squirrel.objects.all()
    fields = ['Unique_Squirrel_Id','Longtitude','Latitude','Date','Shift']
    context = {
        'squirrels': squirrels,
        'fields': fields,
    }
    return render(request, 'sightings/sightings.html', context)

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
    
    else:
        form = SquirrelForm()
    context = {'form': form}
    return render(request, 'sightings/add.html', context)
    
def update(request,unique_squirrel_id):
    sight = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form=SquirrelForm(request.POST, instance=sight)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
            form = SquirrelForm(instance=sight)
    context={'form':form}
    return render(request,'sightings/update.html',context)

def stats(request):
    sights = Squirrel.objects.all()
    sq_nums = Squirrel.objects.count()
    
    # shift
    am_amount = Squirrel.objects.all().filter(shift='AM').count()
    pm_amount = Squirrel.objects.all().filter(shift='PM').count()
    AM_pct = am_amount/(am_amount+pm_amount)
    PM_pct = pm_amount/(am_amount+pm_amount)
    AM_pct = '{:.2%}'.format(AM_pct)
    PM_pct = '{:.2%}'.format(PM_pct)

    #age
    Juvenile_n = sights.filter(age='Juvenile').count()
    Adult_n = sights.filter(age='Adult').count()
    Juvenile_pct = Juvenile_n / (Juvenile_n + Adult_n)
    Juvenile_pct = "{:.2%}".format(Juvenile_pct)
    Adult_pct = Adult_n / (Juvenile_n + Adult_n)
    Adult_pct = "{:.2%}".format(Adult_pct)
    
    #primary_fur_color
    Black_n = sights.filter(primary_fur_color='Black').count()
    Gray_n = sights.filter(primary_fur_color='Gray').count()
    Cinnamon_n = sights.filter(primary_fur_color='Cinnamon').count()
    Black_pct = Black_n / (Black_n+Gray_n+Cinnamon_n)
    Black_pct = "{:.2%}".format(Black_pct)
    Gray_pct = Gray_n / (Black_n+Gray_n+Cinnamon_n)
    Gray_pct = "{:.2%}".format(Gray_pct)
    Cinnamon_pct = Cinnamon_n / (Black_n+Gray_n+Cinnamon_n)
    Cinnamon_pct = "{:.2%}".format(Cinnamon_pct)

    #location
    Above_Ground_n = sights.filter(location='Above Ground').count()
    Ground_Plane_n = sights.filter(location='Ground Plane').count()
    Above_Ground_pct = Above_Ground_n / (Above_Ground_n+Ground_Plane_n)
    Above_Ground_pct = "{:.2%}".format(Above_Ground_pct)
    Ground_Plane_pct = Ground_Plane_n / (Above_Ground_n+Ground_Plane_n)
    Ground_Plane_pct= "{:.2%}".format(Ground_Plane_pct)

    #runs_from
    True_n = sights.filter(runs_from=True).count()
    False_n = sights.filter(runs_from=False).count()
    True_pct = True_n / (True_n+False_n)
    True_pct = "{:.2%}".format(True_pct)
    False_pct = False_n / (True_n+False_n)
    False_pct = "{:.2%}".format(False_pct)
    
    context = {
            'total_squirrel':sq_nums,
            'Shift': {'AM': am_amount,'PM': pm_amount},
            'Shift_pct': {'AM': AM_pct,'PM': PM_pct},
            'Age': {'Juvenile': Juvenile_n, 'Adult': Adult_n},
            'Age_pct': {'Juvenile': Juvenile_pct, 'Adult': Adult_pct},
            'Primary_Fur_Color': {'Black':Black_n, 'Gray':Gray_n, 'Cinnamon':Cinnamon_n},
            'Primary_Fur_Color_pct': {'Black':Black_pct, 'Gray':Gray_pct, 'Cinnamon':Cinnamon_pct},
            'Location': {'Above_Ground':Above_Ground_n, 'Ground_Plane':Ground_Plane_n},
            'Location_pct': {'Above_Ground':Above_Ground_pct, 'Ground_Plane':Ground_Plane_pct},
            'Runs_From': {'True':True_n, 'False':False_n},
            'Runs_From_pct': {'True':True_pct, 'False':False_pct},
            }
    return render(request, 'sightings/stats.html',{'context': context})


def details(request,squirrel_id):
    squirrel = Sighting.objects.get(id = squirrel_id)
    if request.method == 'GET':
        form = SightingForm(instance = squirrel)
    context = {
            'form':form,
    }
    return render(request, 'sightings/details.html', context)

def homepage_view(request):
    return render(request,'sightings/homepage.html')

# def list_sights(request):
#     sights = Squirrel.objects.all()
#     fields = ['Unique_Squirrel_Id','Longtitude','Latitude','Date','Shift']
#     context = {
#             'sights':sights,
#             'fields':fields,
#             }
#     return render(request, 'Tracker/list.html', context)
