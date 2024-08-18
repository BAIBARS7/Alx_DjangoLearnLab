from django.urls import path
from .views import (
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    add_book, edit_book, delete_book,
    user_login, user_logout, user_register,
    admin_view, librarian_view, member_view,
    LibraryDetailView
)

urlpatterns = [
    # Book-related URLs
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/add/', add_book, name="add_book"),
    path('books/<int:pk>/edit/', edit_book, name="edit_book"),
    path('books/<int:pk>/delete/', delete_book, name="delete_book"),

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
