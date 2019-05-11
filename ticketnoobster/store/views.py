from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, Location, Section
from .serializers import EventSerializer, LocationSerializer, SectionSerializer
# Create your views here.

class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class SectionView(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer