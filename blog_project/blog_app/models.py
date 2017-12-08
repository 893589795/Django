from django.db import models

# Create your models here.


class Video(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField(null=True, blank=True)
    url_image = models.URLField(null=True, blank=True)
    cover = models.FileField(upload_to='cover_image', null=True)
    editors_choice = models.BooleanField(default=False)
    likes = models.IntegerField(null=True, blank=True)
    readers = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
