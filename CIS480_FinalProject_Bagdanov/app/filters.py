import django_filters
from .models import Driver

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', ]

