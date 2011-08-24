from django.http import HttpResponse
from dashboard.models import Startup
from dashboard.models import Review
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return HttpResponse("Hello index")
    
def startups(request):
    startup_list = Startup.objects.all().order_by('-date_updated')
    return render_to_response('startups/list.html', {'startup_list': startup_list}, context_instance=RequestContext(request))

def startup_detail(request, startup_id):
    startup = Startup.objects.get(id=startup_id)
    reviews = Review.objects.filter(startup=startup_id)
    return render_to_response('startups/detail_page.html', {'startup': startup, 'reviews': reviews}, context_instance=RequestContext(request))

def review(request, new_review):
    return HttpResponse("New review")

def review_detail(request, review_id):
    return HttpResponse("Review %s" % review_id)

def new_review(request):
    return HttpResponse("New review")
    

def person_detail(request, person_id):
    return HttpResponse("Person %s" % person_id)

def people(request):
    return HttpResponse("People")

def json_startups(request):
    startup_list = Startup.objects.all()
    total=startup_list.count()
    page = 1
    if request.POST.__contains__('page'):
        page = request.POST.__getitem__('page')
    rp = 10
    if request.POST.__contains__('rp'):
        rp = request.POST.__getitem__('rp')
    sortname = 'date_added'
    if request.POST.__contains__('sortname'):
        sortname = request.POST.__getitem__('sortname')
    sortorder = 'desc'
    if request.POST.__contains__('sortorder'):
        sortorder = request.POST.__getitem__('sortorder')
    query = ''
    if request.POST.__contains__('query'):
        query = request.POST.__getitem__('query')
    qtype = ''
    if request.POST.__contains__('qtype'):
        qtype = request.POST.__getitem__('qtype')
    
    if sortorder == 'desc':
        sortname = '-' + sortname
    else:
        sortname = '+' + sortname
    startup_list.order_by(sortname)
    
    if(qtype == 'name'):
        startup_list.filter(name__contains=query)
    if(qtype == 'location'):
        startup_list.filter(location__contains=query)
    
    list_count = startup_list.count()
    
    
    

    return render_to_response('startups/json_list.html', {'startup_list': startup_list,
                                                          'page': page,
                                                          'total': total,
                                                          'list_count': list_count
                                                          
                                                          },
                              context_instance=RequestContext(request))
