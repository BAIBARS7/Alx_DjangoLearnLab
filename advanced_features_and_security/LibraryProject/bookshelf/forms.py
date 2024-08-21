from django import forms
from .models import Book  # Assuming you're using the Book model for this example

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'summary']
