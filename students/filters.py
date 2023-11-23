from django_filters import rest_framework as filters
from authentication.models import Student


# We create filters for each field we want to be able to filter on
class StudentFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    creator__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['name','creator__username']

