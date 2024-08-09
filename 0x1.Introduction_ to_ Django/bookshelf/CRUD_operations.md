 python manage.py shell
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)


>>> from bookshelf.models import Book
>>>
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
1984


>>> retrieved_book = Book.objects.get(id=book.id)
>>> print(retrieved_book)
1984
>>> print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")
Title: 1984, Author: George Orwell, Year: 1949


>>> retrieved_book.title = "Nineteen Eighty-Four"
>>> retrieved_book.save()
>>> print(retrieved_book)
Nineteen Eighty-Four



>>> retrieved_book.delete()
(1, {'bookshelf.Book': 1})
>>>
>>> books = Book.objects.all()
>>> print(books)
<QuerySet [<Book: Nineteen Eighty-Four>]>
>>>
