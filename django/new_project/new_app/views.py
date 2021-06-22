from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import json
import os
# Create your views here.

def home(request):
    return HttpResponse("<H1>Hello django world</H1>")

def greeting(request):
    return HttpResponse("<H1>Greetings form django</H1>")

def date(request):
    return HttpResponse(F"Current date/time is {datetime.now()}")

def print_dict(request):
    return HttpResponse(str({i: i*i for i in range(1,16)}))

def hello_html(request):
    result = {"a": "aa"}
    context = {"key": result, "key_1":5, "key_2": "found"}
    return render(request, 'new_app/index.html', context)

def homepage(request):
    name = "Gohar"
    surname = "Keshishyan"
    if request.method == 'POST':
        print(request.POST)
        a = request.POST
        return HttpResponse(F'{a["fname"]} - {a.get("password")}')
    else:
        return render(request, 'new_app/homepage.html')

def json_file(request):
    path = os.path.join(os.getcwd(), 'sample_json.json')
    with open(path, "r") as file:
        data = json.load(file)
        dict_ = {}
        key = 1
        for item in data['items']:
            dict_[f'key{key}'] = item
            key += 1
    return render(request, 'new_app/json_file.html', dict_)


def user_message(request):
    if request.method == 'POST':
        print(request.POST)
        a = request.POST
        return HttpResponse(F'{a["userinput"]}')
    else:
        return render(request, 'new_app/user_message.html')

