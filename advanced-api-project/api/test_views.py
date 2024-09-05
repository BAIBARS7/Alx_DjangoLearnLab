from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test author
        self.author = Author.objects.create(name='Author 1')

        # Create some test books
        self.book1 = Book.objects.create(title='Book 1', publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title='Book 2', publication_year=2019, author=self.author)

        # Set up the API client
        self.client = APIClient()

    def authenticate(self):
        self.client.login(username='testuser', password='testpassword')

    def test_create_book(self):
        # Authenticate the user
        self.authenticate()

        # Data for creating a new book
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }

        response = self.client.post(reverse('book-create'), data, format='json')

        # Check the status code and data
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # 2 books from setUp, plus the new one
        self.assertEqual(Book.objects.get(id=3).title, 'New Book')

    def test_retrieve_book_list(self):
        response = self.client.get(reverse('book-list'), format='json')
        
        # Check status code and data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return 2 books

    def test_filter_books_by_title(self):
        response = self.client.get(reverse('book-list'), {'title': 'Book 1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_search_books_by_author(self):
        response = self.client.get(reverse('book-list'), {'search': 'Author 1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books_by_publication_year(self):
        response = self.client.get(reverse('book-list'), {'ordering': 'publication_year'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book 2')  # Oldest book first

    def test_update_book(self):
        self.authenticate()

        data = {
            'title': 'Updated Book',
            'publication_year': 2020,
            'author': self.author.id
        }

        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.pk}), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book')

    def test_delete_book(self):
        self.authenticate()

        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book1.pk}))

        # Check the status code
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only 1 book should remain

    def test_create_book_without_authentication(self):
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2022,
            'author': self.author.id
        }

        response = self.client.post(reverse('book-create'), data, format='json')

        # Ensure that a 403 Forbidden status is returned
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_without_authentication(self):
        data = {
            'title': 'Unauthorized Update',
            'publication_year': 2020,
            'author': self.author.id
        }

        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.pk}), data, format='json')

        # Ensure that a 403 Forbidden status is returned
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_without_authentication(self):
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book1.pk}))

        # Ensure that a 403 Forbidden status is returned
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
