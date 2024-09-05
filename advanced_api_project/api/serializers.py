from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure the publication year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested serialization of related books
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

# The BookSerializer serializes all fields of the Book model, allowing
    # conversion between Book model instances and formats like JSON.
    #
    # Custom validation ensures that the publication_year cannot be set to a future year.
        # Custom validation to ensure that the publication_year is not set to a future year.
 # The AuthorSerializer serializes the name of the author and dynamically includes
    # a nested list of related books using the BookSerializer.
    #
    # The nested BookSerializer serializes the related books of an author, which are accessed via the
    # reverse relationship through the 'books' related_name on the ForeignKey field.
