import django_filters 

from .models import *
# from .imports import *

class FooditemFilter(django_filters.FilterSet):
    class Meta:
        model = Fooditem
        fields = ['name']  