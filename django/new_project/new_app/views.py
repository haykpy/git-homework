from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def home(request):
    return HttpResponse("<H1>Hello django world</H1>")

def greeting(request):
    return HttpResponse("<H1>Greetings form django</H1>")

def date(request):
    return HttpResponse(F"Current date/time is {datetime.now()}")

def print_dict(request):
    return HttpResponse({i: i*i for i in range(1,16)})
    # new_dict = {}
    # for i in range(1,16):
    #     new_dict[i]= i*i
    # return HttpResponse(new_dict)


