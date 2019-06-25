from django.db import models


class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    cover = models.URLField()
    isbn = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    published = models.DateTimeField()
    publisher = models.CharField(max_length=255, blank=True, default='')
    pages = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, default='')
    website = models.URLField(blank=True, default='')
    author = models.CharField(max_length=255)
