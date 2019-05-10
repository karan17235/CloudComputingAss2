from django.conf.urls import url
from . import views

urlpatterns = [
        # /login/
        url(r'^$' , views.home, name='home'),
        url(r'^home/', views.home, name='home'),
        # /website/register
        url(r'^register/', views.register, name='register'),
        # /website/about/
        url(r'^about/', views.about, name='about'),
        # /website/team
        url(r'^team/', views.team, name='team'),
        url(r'^git/', views.git, name='git'),
        # scenarios
        url(r'^scenario1/', views.scenario1, name='scenario1'),
        url(r'^scenario2/', views.scenario2, name='scenario2'),
        url(r'^scenario3/', views.scenario3, name='scenario3')
]
