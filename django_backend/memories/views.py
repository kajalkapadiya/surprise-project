from django.shortcuts import render

from rest_framework import viewsets
from .models import Event, GalleryPhoto, LoveLetter
from .serializers import EventSerializer, GalleryPhotoSerializer, LoveLetterSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by("date")
    serializer_class = EventSerializer

class GalleryPhotoViewSet(viewsets.ModelViewSet):
    queryset = GalleryPhoto.objects.all().order_by("-id")
    serializer_class = GalleryPhotoSerializer

class LoveLetterViewSet(viewsets.ModelViewSet):
    # we only need latest letter usually, but expose full CRUD via API
    queryset = LoveLetter.objects.all().order_by("-created_at")
    serializer_class = LoveLetterSerializer
