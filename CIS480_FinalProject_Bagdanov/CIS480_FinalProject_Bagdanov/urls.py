"""
Definition of urls for CIS480_FinalProject_Bagdanov.
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from datetime import datetime
import django.contrib.auth.views
from django.http import HttpResponseRedirect

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^administration/$', app.views.administration, name='administration'),
    url(r'^billing/$', app.views.billing, name='billing'),
    url(r'^collections/$', app.views.collections, name='collections'),
    url(r'^customerservice/$', app.views.customerservice, name='customer service'),
    url(r'^fieldservice/$', app.views.fieldservice, name='field service'),
    url(r'^upload/$', app.views.upload, name='upload'),
    url(r'^search/$', app.views.search, name='search'),
    url(r'^calendar/$', app.views.calendar, name='calendar'),
    url(r'^upload/success/$', app.views.success, name='success'),


    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
