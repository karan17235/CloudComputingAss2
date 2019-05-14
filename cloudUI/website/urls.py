from django.conf.urls import url
from . import views

urlpatterns = [
        # url(r'^$' , views.home, name='home'),
        url(r'^$' , views.startimg, name='start'),
        url(r'^home/', views.home, name='home'),
        # /website/about/
        url(r'^about/', views.about, name='about'),
        # /website/team
        url(r'^team/', views.team, name='team'),
        url(r'^git/', views.git, name='git'),
        # scenarios
        url(r'^trend/', views.trend, name='trend'),
        url(r'^content/', views.content, name='content'),
        url(r'^profile/', views.profile, name='profile'),
        # /website/georep
        url(r'^georep', views.georep, name='georep'),
        # /website/youtube
        url(r'^youtube', views.youtube, name='youtube'),
        # /website/group
        url(r'^group', views.group, name='group'),
        # /website/projectreport
        url(r'^projectreport', views.projectreport, name='projectreport'),
]
