from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, GalleryPhotoViewSet, LoveLetterViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")
router.register(r"photos", GalleryPhotoViewSet, basename="photo")
router.register(r"letters", LoveLetterViewSet, basename="letter")

urlpatterns = [
    path("api/", include(router.urls)),
]
