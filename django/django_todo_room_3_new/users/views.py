from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import UserLoginForm
from django.http import HttpResponse

# Create your views here.


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    context = {'form': form}
    return render(request, 'users/register.html', context)


def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('Not Found')
    else:
        return render(request, 'users/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')
