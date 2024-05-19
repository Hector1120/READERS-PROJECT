from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    genre = models.CharField(max_length=100, blank=True, null=True)
    published_year = models.IntegerField(blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cover_image_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
