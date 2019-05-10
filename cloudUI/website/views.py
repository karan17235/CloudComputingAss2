from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'website/register.html', {'form': form})

def home(request):
    return render(request, "website/home.html", {})

def git(request):
    return redirect('https://github.com/pallsac/CloudAssignment2')

def team(request):
    return render(request, "website/team.html", {})

def login(request):
    return render(request, "website/login.html", {})

def about(request):
    return render(request, "website/about.html", {})

def scenario1(request):
    return render(request, "website/about.html", {})
def scenario2(request):
    return render(request, "website/about.html", {})
def scenario3(request):
    return render(request, "website/about.html", {})