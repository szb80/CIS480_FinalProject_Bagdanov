"""
Definition of forms.
"""

from django import forms
from django.forms import ModelForm, Textarea
from datetime import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from .models import *

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        fields = ['title', 'description', 'department', 'tags', 'source_file', ]
        #widgets = { 'description': Textarea(), }


##################################################################################

class adddriverform(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', 'dob', 'city', 'car_make', 'car_model']
        widgets = {'dob': SelectDateWidget(years=range((datetime.now().year - 14),1900,-1))}

