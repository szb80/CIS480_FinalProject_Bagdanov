from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Document)


#####################################################################
admin.site.register(CarMake)
admin.site.register(Driver)