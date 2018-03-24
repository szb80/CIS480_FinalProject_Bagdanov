"""
Definition of views.
"""

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, render, render_to_response
from django.template import RequestContext
from datetime import datetime
from django.utils import timezone
from django.views.generic.edit import CreateView

from .models import Document, Department
from .forms import *
import json

def get_department(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    depts = Department.objects.filter(name__icontains=q)
    results = []
    for d in depts:
      d_json = {}
      d_json = d.name
      results.append(d_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

# search view 
def search(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:            
            results = Document.objects.filter(  
            	Q( title__contains = q ) |
                Q( description__contains = q ) |
                Q( description__contains = q )
                )          
            return render_to_response('results.html', {'results': results}, 
                                       context_instance = RequestContext(request))


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def administration(request):
    """Renders the administration page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/administration.html',
        {
            'title':'Administration',
            'year':datetime.now().year,
        }
    )

def billing(request):
    """Renders the billing page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/billing.html',
        {
            'title':'Billing',
            'message':'Your billing page.',
            'year':datetime.now().year,
        }
    )

def collections(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/collections.html',
        {
            'title':'Collections',
            'message':'Your collections page.',
            'year':datetime.now().year,
        }
    )

def customerservice(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/customer_service.html',
        {
            'title':'Customer Service',
            'message':'Your Customer Service page.',
            'year':datetime.now().year,
        }
    )

def fieldservice(request):
    """Renders the field service page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/field_service.html',
        {
            'title':'Field Service',
            'message':'Your Field Service page.',
            'year':datetime.now().year,
        }
    )

def search(request):
    """Renders the field service page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/searchtest.html',
        {
            'title':'Search Test',
            'message':'Your search page.',
            'year':datetime.now().year,
        }
    )

def calendar(request):
    """Renders the calendar page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/calendar.html',
        {
            'title':'Calendar Page',
            'year':datetime.now().year,
        }
    )

############################################################################
def default(request):
    """Renders the field service page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/default.html',
        {
            'title':'Default',
            'message':'Your default page format.',
            'year':datetime.now().year,
        }
    )

def documentationdetail(request):
    """Renders the field service page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/documentationdetail.html',
        {
            'title':'Documentation Detail',
            'message':'Your documentation detail page format.',
            'year':datetime.now().year,
        }
    )

def upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Without this next line the tags won't be saved.
            form.save_m2m()
            return HttpResponseRedirect('app/success.html')

        # validate form and save if success
        #if form.is_valid():
            #form.save()
            #form.save_m2m()
            #return HttpResponseRedirect('app/success.html') # send to success page
        else: # form was invalid and send to error page
            return render(request, "app/error.html",) 


    elif request.method == "GET":
        form = DocumentForm()
    return render(request, "app/upload.html", {'form': form})


#############################################################################
def adddriver(request):
    if request.method == "POST":
        form = adddriverform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return HttpResponseRedirect('/roster/')
        else:
            return HttpResponseRedirect('/')

    elif request.method == "GET":
        form = adddriverform()
        return render(request, "app/registerdriver.html", {'form': form})

#################################################################################
