from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})


class OrderView(ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = OrderSerializer



def orders_app(request):
    return render(request, 'main_app.html')
