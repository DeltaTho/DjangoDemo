from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Exhibit

#This is an obsolete file - We now have generic views implemented, and do not need to detect mobile os on the server side at all
#Since the templates are now running bootstrap to create a reactive teplate.  

# list of mobile User Agents
mobile_uas = [
	'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
	'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
	'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
	'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
	'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
	'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
	'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
	'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
	'wapr','webc','winw','winw','xda','xda-'
	]
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]
 
#Super simple device detection, returns True for mobile devices
def mobileBrowser(request):

 
    mobile_browser = False
    ua = request.META['HTTP_USER_AGENT'].lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser




# Create your views here.
#------------------------
#Lists all exhibits in DB
def index(request):
    exhibit_list = Exhibit.objects.order_by('exhibit_title')
    template = loader.get_template('exhibits/index.html')
    context = {
        'exhibit_list':exhibit_list,
    }
    if (mobileBrowser(request)):
        return render(request, 'exhibits/m_index.html', {'exhibit_list': exhibit_list})
    else:
        return render(request, 'exhibits/index.html', {'exhibit_list': exhibit_list})

#future home of search results
def results(request, search_term):
    result_list = Exhibit.objects.filter(exhibit_title=search_term)

    if (mobileBrowser(request)):
        return render(request, 'exhibits/m_results.html', {'results':result_list})
    else:
        return render(request, 'exhibits/results.html', {'results':result_list})

#Generates page for a specific exhibit
def detail(request, exhibit_id):

    exhibit = get_object_or_404(Exhibit, pk=exhibit_id)

    if (mobileBrowser(request)):
        return render(request, 'exhibits/m_detail.html', {'exhibit': exhibit})
    else:
        return render(request, 'exhibits/detail.html', {'exhibit': exhibit})


#returns a list of exhibits no longer than max_number
def sidenav(request):

    max_number = 5

    exhibit_list = Exhibit.objects.order_by('exhibit_title')[:max_number]
    template = loader.get_template('exhibits/index.html')
    context = {
        'exhibit_list':exhibit_list,
    }
    return render(request, 'exhibits/sidenav.html', {'exhibit_list': exhibit_list})