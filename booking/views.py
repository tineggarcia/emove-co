from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Booking Home</h1>')

# Create your views here.
