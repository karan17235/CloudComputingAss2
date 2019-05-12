# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import json
import couchdb
import time
from django.shortcuts import render, redirect
from django.http import HttpResponse

#from .models import Profile, Trend, Content
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

def trend(request):
    trend_list = {}
    #Trend.objects.filter(trend_name="trend").delete()
    user = "admin"
    password = "admin"
    
    couchserver = couchdb.Server("http://%s:%s@172.26.38.45:5984/" % (user,password))
    db_name = {'adelaide': ['immigrant_adelaide', 'all_keywords_adelaide', 'immigrant_adelaide', 'profile_analysis','trend_analysis'], 'brisbane': ['immigrant_brisbane', 'all_keywords_brisbane', 'immigrant_brisbane', 'profile_analysis','trend_analysis'], 'canberra': ['immigrant_canberra', 'all_keywords_canberra', 'immigrant_canberra', 'profile_analysis','trend_analysis'], 'melbourne': ['immigrant_melbourne', 'all_keywords_melbourne', 'immigrant_melbourne', 'profile_analysis','trend_analysis'], 'perth': ['immigrant_design', 'all_keywords_perth', 'immigrant_view', 'profile_analysis_view','trend_analysis'], 'sydney': ['immigrant_sydney', 'all_keywords_sydney', 'immigrant_sydney', 'profile_analysis','trend_analysis']}

    #City Wise Data
    trend_count = {'adelaide': [0,0],'brisbane':[0,0],'canberra':[0,0],'melbourne':[0,0],'perth': [0,0],'sydney':[0,0]}
    for dbname,design_name in db_name.items():
        db = couchserver[dbname]
        print(dbname)
        para = (design_name[0]+'/'+design_name[2])
        flag = True
        while flag:
            try:
                for item in db.view(para, group=True):
                    trend_count[dbname][1] += item.value
                trend_count[dbname][0]=(db.info()['doc_count'])
                print(trend_count)
                flag = False
            except couchdb.http.ServerError:
                print("Retrying")
                time.sleep(3*60)
        trend_list['city'] = trend_count
    
    # Month Wise Data
    trend_count = {'Jan': 0,'Feb':0,'Mar':0,'Apr':0,'May': 0,'Jun':0,'Jul':0,'Aug':0,'Sep': 0,'Oct':0,'Nov':0,'Dec':0}
    for dbname,design_name in db_name.items():
        db = couchserver[dbname]
        print(dbname)
        para = (design_name[0]+'/'+design_name[4])
        flag = True
        while flag:
            try:
                for item in db.view(para, group=True, group_level=1):
                    date = item.key[0].split()
                    print(date[1],date[5])
                    trend_count[date[1]] += item.value

                print(trend_count)
                flag = False
            except couchdb.http.ServerError:
                print("Retrying")
                time.sleep(3*60)
        trend_list['month'] = trend_count
    print(trend_list)
    return render(request, "website/trend.html", {'trend_list':trend_list})

def scenario2(request):
    return render(request, "website/about.html", {})

def scenario3(request):
    return render(request, "website/about.html", {})

def georep(request):
    return render(request, "website/georep.html", {})