from django.views import generic
from django.shortcuts import render, redirect
from .models import Exhibit
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#We don't have a home page yet so this redirects our TLD to index
def home(request):
    return redirect('/exhibits/')

#lists all items in DB
class IndexView(generic.ListView):
    template_name = 'exhibits/index.html'
    paginate_by = 5 # number of results per page

    def get_queryset(self):
        return Exhibit.objects.all()

#provides details on a specific item in the db
class DetailView(generic.DetailView):
    model = Exhibit
    template_name = 'exhibits/detail.html'

#handles our search queries
def search(request):
    exhibits_list = Exhibit.objects.all()
    query = request.GET.get('q')

    if query:
        exhibits_list = Exhibit.objects.annotate(
        search=SearchVector('exhibit_title') + SearchVector('exhibit_description'),
        ).filter(search = SearchQuery(query) & SearchQuery(query))

    paginator = Paginator(exhibits_list,5) #5 results per page
    page = request.GET.get('page')

    try:
        exhibits = paginator.page(page)
    except PageNotAnInteger:
        exhibits = paginator.page(1)
    except EmptyPage:
        exhibits = paginator.page(paginator.num_pages)

    context = dict(results = exhibits, q = query)
    return render(request, "exhibits/results.html", context)
    
