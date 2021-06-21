from django.http import HttpResponse

from django.shortcuts import render

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

from django.urls import reverse

from django.views import generic

from django.utils import timezone


def index(request):
    return render(request,'home/index.html')

def results1(request, pk):
    return render(request,'home/results1.html')

def results2(request, pk):
    return render(request,'home/results2.html')

def results3(request, pk):
    return render(request,'home/results3.html')

def us(request, pk):
    return render(request,'home/us.html')


def orders(request, pk):
    return render(request,'home/orders.html')
    
