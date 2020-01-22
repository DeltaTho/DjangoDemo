from django.conf.urls import url
from django.conf.urls import include
from . import views

app_name = 'exhibits'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^exhibits/$', views.IndexView.as_view(), name='index'),
    url(r'^exhibits/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^search?$', views.search, name='search')
]

