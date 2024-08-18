from django.urls import path
from . import views
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from .views import add_book, edit_book, delete_book

urlpatterns = [
    # URLs for books
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),

    # URLs for library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # URLs for user authentication
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),

    # URLs for role-based views
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]
