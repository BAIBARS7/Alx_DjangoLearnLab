from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return None

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Sample usage
if __name__ == "__main__":
    # Query all books by a specific author
    books_by_author = get_books_by_author("J.K. Rowling")
    if books_by_author:
        print("Books by J.K. Rowling:")
        for book in books_by_author:
            print(book.title)
    else:
        print("No books found for J.K. Rowling")

    # List all books in a library
    books_in_library = get_books_in_library("Central Library")
    if books_in_library:
        print("\nBooks in Central Library:")
        for book in books_in_library:
            print(book.title)
    else:
        print("No books found in Central Library")

    # Retrieve the librarian for a library
    librarian = get_librarian_for_library("Central Library")
    if librarian:
        print(f"\nLibrarian for Central Library: {librarian.name}")
    else:
        print("No librarian found for Central Library")
