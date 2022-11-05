from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    s

