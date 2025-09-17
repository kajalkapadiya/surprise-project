from rest_framework import serializers
from .models import Event, GalleryPhoto, LoveLetter

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class GalleryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPhoto
        fields = "__all__"

class LoveLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoveLetter
        fields = "__all__"
