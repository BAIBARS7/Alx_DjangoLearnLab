from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import redirect
from .models import Book

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle book creation logic
        pass
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        # Handle book editing logic
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/confirm_delete.html', {'book': book})

# CSRF and session cookies are secured to only be transmitted over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
