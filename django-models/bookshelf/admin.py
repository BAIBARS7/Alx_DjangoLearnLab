from django.contrib import admin
from .models import Book

# Register the Book model with the admin site
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Customize the list display in the admin
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality for title and author fields
    search_fields = ('title', 'author')
    
    # Add filter options for publication_year
    list_filter = ('publication_year',)
