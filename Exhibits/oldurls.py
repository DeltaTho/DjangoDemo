from django.urls import path
from . import views

##we are currently using reg expressions in the new urls
#so this is effectively obsolete.

app_name = 'exhibits'

urlpatterns = [
    #/exhibits
    path('', views.index, name='index'),
    #/exhibits/id
    path('<int:exhibit_id>/',views.detail, name='detail'),
    #/exhibits/id/results
    path('results/',views.results, name='results'),
    
]