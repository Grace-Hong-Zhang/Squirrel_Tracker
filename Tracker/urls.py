from . import views
from django.urls import path

urlpatterns = [
        path("", views.homepage_view),
        path('map/', views.map),
        path('sightings/', views.sightings),
        path('sightings/add/', views.add, name = 'add'),
        path('sightings/stats/', views.stats, name = 'stats'),
        path('sightings/<str:unique_squirrel_id>/details/', views.details, name= 'details'),
        path('sightings/<str:unique_squirrel_id>/', views.update, name = 'update'),
        ]