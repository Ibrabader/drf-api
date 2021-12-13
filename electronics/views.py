from django.shortcuts import render
from rest_framework import generics 
from .serializers import ElectronicsSerializers
from .models import Electronics 
from .permissions import IsAuthenticatedOrReadOnly


class ElectronicsList(generics.ListCreateAPIView):
    queryset = Electronics.objects.all()
    serializer_class = ElectronicsSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
class ElectronicsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Electronics.objects.all()
    serializer_class = ElectronicsSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)