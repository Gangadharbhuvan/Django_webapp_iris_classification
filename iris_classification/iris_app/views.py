from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    return render(request, 'iris_app/index.html')

def form_name_view(request):
    form = forms.FormName()
    return render(request, 'iris_app/prediction.html', {'form' : form})

