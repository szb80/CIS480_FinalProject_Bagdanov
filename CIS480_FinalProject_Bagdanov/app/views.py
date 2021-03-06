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
from .filters import DocumentFilter
import json

def search(request):
    document_list = Document.objects.all()
    document_filter = DocumentFilter(request.GET, queryset=document_list)
    return render(request, 'app/document_list.html', {'filter': document_filter})

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
    documents_administration = Document.objects.filter(department__exact=1, )
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/department_template.html',
        {
            'title':'Administration',
            'year':datetime.now().year,
            'filelist':documents_administration,
        }
    )

def billing(request):
    """Renders the administration page."""
    documents_billing = Document.objects.filter(department__exact=2, )
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/department_template.html',
        {
            'title':'Billing',
            'year':datetime.now().year,
            'filelist':documents_billing,
        }
    )

def collections(request):
    """Renders the administration page."""
    documents_collections = Document.objects.filter(department__exact=3, )
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/department_template.html',
        {
            'title':'Collections',
            'year':datetime.now().year,
            'filelist':documents_collections,
        }
    )

def customerservice(request):
    """Renders the administration page."""
    documents_customerservice = Document.objects.filter(department__exact=4, )
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/department_template.html',
        {
            'title':'Customer Service',
            'year':datetime.now().year,
            'filelist':documents_customerservice,
        }
    )

def fieldservice(request):
    """Renders the administration page."""
    documents_fieldservice = Document.objects.filter(department__exact=5, )
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/department_template.html',
        {
            'title':'Field Service',
            'year':datetime.now().year,
            'filelist':documents_fieldservice,
        }
    )

def success(request):
    """Renders the field service page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/success.html',
        {
            'title':'Success',
            'message':'The file was successfully uploaded.',
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

def upload(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            # Without this next line the tags won't be saved.
            form.save_m2m()
            return render(request, 'app/success.html', {'document':obj}, )

        else: # form was invalid and send to error page
            return render(request, 'error.html',) 

    elif request.method == "GET":
        form = DocumentForm()
    return render(request, "app/upload.html", {'form': form})
