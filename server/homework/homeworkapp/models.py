from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    age = models.CharField(null=True, blank=True, max_length=200)
    sex = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        self.name
