from django.shortcuts import render

# Create your views here.
from .models import Order
from  django_filters.rest_framework import DjangoFilterBackend ,filters
from .serializer import OrderSerializer
from rest_framework import generics

from rest_framework import filters


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['type']
    search_fields = ['cust_name' ,'product_name', 'type']
    ordering_fields = ['discout']













#     queryset = Order.objects.all()
#     #filters.SearchFilter
#     serializer_class = OrderSerializer
#     filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
#    # ordering_fields = ['discount']
#    # filterset_fields = ['category', 'in_stock']
   
#     search_fields = ['cust_name' ,'product_name','type']
