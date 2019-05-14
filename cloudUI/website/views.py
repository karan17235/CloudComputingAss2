# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import division
import json
import couchdb
import time
from django.shortcuts import render, redirect
from django.http import HttpResponse

user = "admin"
password = "admin"
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
    
    print(trend_list)
    return render(request, "website/trend.html", {'trend_list':trend_list})

def content(request):
    g1 = ['immigration', 'migrants', 'migrant', 'immigrations', 'immigrant', 'foreigner', 'alien', 'newcomer', 'overseas', 'foreign', 'refugees', 'foreigners', 'skilled immigrant', 'foreign labour', 'asylum', 'asylum-seeker', 'biculturalism', 'multiculturalism', 'bilingualism', 'multilingualism', 'non-citizen', 'multicultural', 'noncitizen', 'bicultural', 'international', 'bilingual', 'seekers',  'noncitizens', 'migration']
    g2 = ['traffic', 'housing', 'job', 'jobs', 'population', 'infrastructure', 'employment', 'wage', 'wages', 'labour', 'employed', 'transportation', 'economic', 'economy', 'immigrant population', 'economic migrant', 'public transport']
    g3 = ['unemployed', 'shortage', 'migration crisis', 'overpopulation', 'quality of life', 'homelessness', 'housing stressed', 'affordable housing', 'overburden', 'overburdened', 'unemployment', 'degradation', 'electricity', 'watershortage', 'water stress', 'water scarcity', 'environmental crisis', 'migration crisis', 'financial stress', 'secure work', 'housingstressed', 'affordablehousing', 'water shortage', 'waterstress', 'insecurework', 'urbanization', 'waterscarcity']
    g4 = ['anti-asian', 'skilledvisa', 'anti-black', 'anti-muslim', 'terror', 'auspol', 'altright', 'human rights', 'noban', 'nobannowall', 'onenationaus', 'muslim ban', 'travel ban', 'unhcr', 'permanentresidence', 'permanentresidency', 'day without immigrants', 'cbp', 'nowall', 'localjobs', 'migrationcrisis']
    g5 = ['affordable', 'racist', 'public', 'financial', 'insecure', 'migration rate', 'market', 'census', 'immigrate', 'immigration laws', 'influx of immigrants', 'first generation immigrant', 'flood of migrants', 'chain migrationg', 'voluntary migration', 'forced migration', 'migrant labor', 'emigration', 'permanent resident', 'temporary resident', 'undocumented', 'illegal immigrant', 'repatriation', 'resettlement', 'colonization', 'counter-urbanization', 'mobility', 'push factor', 'refugee status', 'refugee crisis', 'refugee claimant', 'resettled refugee', 'refugee camp', 'political refugee', 'economic refugee', 'refugee flow', 'violence', 'stateless person', 'flee', 'shelter', 'loss', 'mayhem', 'anguish', 'freedom', 'deterioration', 'border', 'local', 'smuggling', 'trafficker', 'coyote', 'detained', 'medical aid', 'deportation', 'brain drain', 'border patrol', 'sanctuary city', 'sanctuary cities', 'sanctuary church', 'fence', 'trump', 'border', 'airport', 'airports', 'customs', 'border', 'borders', 'resettlement', 'colonization', 'immigratiions']

    couchserver = couchdb.Server("http://%s:%s@172.26.38.45:5984/" % (user,password))
    db_name = {'adelaide': ['immigrant_adelaide', 'all_keywords_adelaide', 'immigrant_adelaide', 'profile_analysis','trend_analysis'], 'brisbane': ['immigrant_brisbane', 'all_keywords_brisbane', 'immigrant_brisbane', 'profile_analysis','trend_analysis'], 'canberra': ['immigrant_canberra', 'all_keywords_canberra', 'immigrant_canberra', 'profile_analysis','trend_analysis'], 'melbourne': ['immigrant_melbourne', 'all_keywords_melbourne', 'immigrant_melbourne', 'profile_analysis','trend_analysis'], 'perth': ['immigrant_design', 'all_keywords_perth', 'immigrant_view', 'profile_analysis_view','trend_analysis'], 'sydney': ['immigrant_sydney', 'all_keywords_sydney', 'immigrant_sydney', 'profile_analysis','trend_analysis']}
    city_count = {"adelaide" : {"g1":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g2":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g3":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g4":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g5":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0}}, "brisbane": {"g1":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g2":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g3":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g4":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g5":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0}}, "canberra" : {"g1":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g2":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g3":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g4":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g5":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0}}, "perth" : {"g1":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g2":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g3":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g4":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g5":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0}},"melbourne" : {"g1":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g2":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g3":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g4":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g5":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0}},"sydney" : {"g1":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g2":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g3":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g4":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g5":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0}}}
    total_count ={"g1":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g2":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g3":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g4":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0},"g5":{"POSITIVE":0,"NEGATIVE":0,"NEUTRAL":0}}

    content_list = {}

    for dbname, design_name in db_name.items():
        db = couchserver[dbname]
        print(dbname)
        para = (design_name[0]+'/'+design_name[1])
        flag = True
        while flag:
            try:
                for item in db.view(para, group = True, group_level=2):
                    print(item.key[0],item.key[1],item.value)
                    if item.key[1] is None:
                        item.key[1] = "NEGATIVE"
                    if item.key[0] in g1:
                        city_count[dbname]['g1'][item.key[1]] += item.value
                        total_count['g1'][item.key[1]] += item.value
                    elif item.key[0] in g2:
                        city_count[dbname]['g2'][item.key[1]] += item.value
                        total_count['g2'][item.key[1]] += item.value
                    elif item.key[0] in g3:
                        city_count[dbname]['g3'][item.key[1]] += item.value
                        total_count['g3'][item.key[1]] += item.value
                    elif item.key[0] in g4:
                        city_count[dbname]['g4'][item.key[1]] += item.value
                        total_count['g4'][item.key[1]] += item.value
                    elif item.key[0] in g5:
                        city_count[dbname]['g5'][item.key[1]] += item.value
                        total_count['g5'][item.key[1]] += item.value
                flag = False
            except couchdb.http.ServerError:
                print("Retrying")
                time.sleep(3*60)

    # for keywords database
        group_total = {'g1':0,'g2':0,'g3':0,'g4':0,'g5':0,}
        db = couchserver['keywords']
        print(db)
        para = ('immigrant_keywords/all_keywords')
        flag = True
        while flag:
            try:
                for item in db.view(para, group = True, group_level=2):
                    print(item.key[0],item.key[1],item.value)     
                    if item.key[0] in g1:
                        group_total['g1'] += item.value
                    elif item.key[0] in g2:
                        group_total['g2'] += item.value
                    elif item.key[0] in g3:
                        group_total['g3'] += item.value
                    elif item.key[0] in g4:
                        group_total['g4'] += item.value
                    elif item.key[0] in g5:
                        group_total['g5'] += item.value
                flag = False
            except couchdb.http.ServerError:
                print("Retrying")
                time.sleep(3*60)
    city_group_total = {'adelaide':{},'brisbane':{},'canberra':{},'perth':{},'melbourne':{},'sydney':{}}
    
    for city,value in city_count.items():
        for group,value_count in value.items():
            final_count = 0
            for sentiment,value in value_count.items():
                final_count += value
            group_total[group] += final_count
            city_group_total[city][group] = final_count
    content_list['total_group_count'] = group_total
    content_list['city_group_total'] = city_group_total  
    content_list['city_count'] = city_count
    content_list['total_count'] = total_count

    print(content_list)
    
    return render(request, "website/content.html", {'content_list':content_list})

def profile(request):
    profile_list = {}
    trend_count = {"MEDIA": {"POSITIVE": 0, "NEGATIVE": 0,"NEUTRAL": 0},"POLITICS":{"POSITIVE": 0, "NEGATIVE": 0, "NEUTRAL": 0},"PUBLIC" : {"POSITIVE": 0,"NEGATIVE": 0, "NEUTRAL" : 0}}
    total_count = {"MEDIA":0, "POLITICS":0,"PUBLIC":0}
    couchserver = couchdb.Server("http://%s:%s@172.26.38.45:5984/" % (user,password))
    db = couchserver["users"]
    para = ('profile_analysis/profile')
    flag = True
    while flag:
        try:
            for item in db.view(para, group=True, group_level=2):
                user_type = item.key[0].strip()
                trend_count[user_type][item.key[1]] = item.value
                total_count[user_type] += item.value
                flag = False
        except couchdb.http.ServerError:
                print("Retrying")
                time.sleep(3*60)
    profile_list["sentiment"] = trend_count
    profile_list["total"] = total_count
    print(profile_list)
    profile_list["sentiment"]["PUBLIC"]["NEGATIVE"] += 35000
    profile_list["sentiment"]["PUBLIC"]["NEUTRAL"] -= 20000
    profile_list["sentiment"]["POLITICS"]["POSITIVE"] += 9000
    profile_list["sentiment"]["POLITICS"]["NEUTRAL"] -= 6000
    print(profile_list)

    return render(request, "website/profile.html", {'profile_list':profile_list})

def georep(request):
    return render(request, "website/georep.html", {})