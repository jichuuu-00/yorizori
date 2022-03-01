from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

def MainSearch(request) :
    return render(request, 'articleapp/list.html')


