import django_filters
from .models import Document

class DocumentFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Document
        fields = ['department', 'title', 'description', ]
