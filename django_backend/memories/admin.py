from django.contrib import admin
from .models import Event, GalleryPhoto, LoveLetter

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("date", "title")
    ordering = ("-date",)

@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ("caption", "image")

@admin.register(LoveLetter)
class LoveLetterAdmin(admin.ModelAdmin):
    list_display = ("created_at",)
