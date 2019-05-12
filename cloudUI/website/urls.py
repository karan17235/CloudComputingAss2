from django.conf.urls import url
from . import views

urlpatterns = [
        # /login/
        url(r'^$' , views.home, name='home'),
        url(r'^home/', views.home, name='home'),
        # /website/about/
        url(r'^about/', views.about, name='about'),
        # /website/team
        url(r'^team/', views.team, name='team'),
        url(r'^git/', views.git, name='git'),
        # scenarios
        url(r'^trend/', views.trend, name='trend'),
        url(r'^scenario2/', views.scenario2, name='scenario2'),
        url(r'^scenario3/', views.scenario3, name='scenario3'),
        # /website/georep
        url(r'^georep', views.georep, name='georep'),
]
