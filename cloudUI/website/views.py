from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


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
    return render(request, "website/scenario1.html", {})
def scenario2(request):
    return render(request, "website/about.html", {})
def scenario3(request):
    return render(request, "website/about.html", {})

def georep(request):
    return render(request, "website/georep.html", {})