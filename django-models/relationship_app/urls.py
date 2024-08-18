from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    add_book, edit_book, delete_book,
    user_login, user_logout, user_register,
    admin_view, librarian_view, member_view,
    LibraryDetailView,
)
from .views import list_books

urlpatterns = [
    # Book-related URLs
    path('list_books/', BookListView.as_view(), name="book_list"),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('add_book/add/', add_book, name="add_book"),
    path('edit_book/<int:pk>/edit/', edit_book, name="edit_book"),
    path('delete_book/<int:pk>/delete/', delete_book, name="delete_book"),

    path('list_books/', list_books, name='list_books'),

    # Library detail URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # User authentication URLs
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),

    # Role-based views URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
