import django_filters
from .models import Driver, Document

class UserFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Driver
        fields = ['first_name', 'last_name', ]


class DocumentFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Document
        fields = ['department', 'title', 'description', ]
