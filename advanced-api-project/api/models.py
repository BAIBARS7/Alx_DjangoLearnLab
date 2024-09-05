from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# The Author model represents a book author. It contains the name of the author,
    # and is related to the Book model through a one-to-many relationship. 
    # Each author can have multiple books.
     # The Book model represents a book. It contains the title of the book, 
    # the publication year, and a foreign key that links the book to an author.
    # The foreign key establishes a one-to-many relationship, where an author can have multiple books.
