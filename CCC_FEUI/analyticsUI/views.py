from django.shortcuts import render
from django.http import HttpResponse

from .models import AnalyticsUI

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Analytics')

    analyticsui = AnalyticsUI.objects.all()[:10]

    context = {
        'title': 'Latest Analytics Views',
        'analyticsui': analyticsui
    }

    return render(request, 'analyticsUI/index.html', context)

def details(request, id):
    analyticsui = AnalyticsUI.objects.get(id=id)

    context = {
        'analyticsui': analyticsui
    }

    return render(request, 'analyticsUI/details.html', context)