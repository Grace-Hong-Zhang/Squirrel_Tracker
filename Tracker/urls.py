from . import views
from django.urls import path

urlpatterns = [
        path('map/', views.map),
        path('sightings/', views.sightings),
        path('sightings/add/', views.add, name = 'add'),
        path('sightings/stats/', views.stats, name = 'stats'),
        path('sightings/sightings/<int:squirrel_id>/', views.details),
        path('sightings/<str:unique_squirrel_id>/', views.update, name = 'update'),
        ]