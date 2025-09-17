from django.db import models

# Create your models here.

class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to="events/", blank=True, null=True)

    def __str__(self):
        return f"{self.date} - {self.title}"

class GalleryPhoto(models.Model):
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.caption or f"Photo {self.pk}"

class LoveLetter(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # short preview
        return (self.content[:50] + "...") if len(self.content) > 50 else self.content
