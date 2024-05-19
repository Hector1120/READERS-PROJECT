from django import forms
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title',
                'author',
                'genre',
                'published_year',
                'isbn',
                'publisher',
                'pages',
                'language',
                'description',
                'cover_image_url',
                'status']
