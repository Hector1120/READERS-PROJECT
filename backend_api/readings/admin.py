from django.contrib import admin
from.models import Books

# Register your models here.

# Register your models here.
class BooksFields(admin.ModelAdmin):
    list_display = (
                'title',
                'author',
                'genre',
                'published_year',
                'isbn',
                'publisher',
                'pages',
                'language',
                'description',
                'cover_image_url',
                'status',
            )
admin.site.register(Books, BooksFields)

