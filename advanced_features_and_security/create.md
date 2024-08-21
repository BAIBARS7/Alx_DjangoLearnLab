# Create Operation

**Command:**

```python
from book_library.models import Book

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
