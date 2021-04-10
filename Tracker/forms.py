from django import forms
from django.forms import fields, widgets, ModelForm
from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'