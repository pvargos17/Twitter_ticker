from django.shortcuts import render
from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer, LoadSerializer

# Create your views here.
class ListCompanyView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ListLoadView(generics.ListAPIView):

    query = Load.objects.all()
    serializer = LoadSerializer
