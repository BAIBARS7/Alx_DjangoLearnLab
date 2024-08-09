>>> retrieved_book.delete()
(1, {'bookshelf.Book': 1})
>>>
>>> books = Book.objects.all()
>>> print(books)
<QuerySet [<Book: Nineteen Eighty-Four>]>
>>>
