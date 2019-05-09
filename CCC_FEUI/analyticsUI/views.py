from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Analytics')

    return render(request, 'analyticsUI/index.html', {
        'title': 'Latest Analytics Views'
    })