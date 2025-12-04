from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
       
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        
        self.author1 = Author.objects.create(name="George Orwell")
        self.author2 = Author.objects.create(name="J.K. Rowling")

        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author1)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author1)
        self.book3 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author2)

    # ------------------ CRUD Tests ------------------

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2023, 'author': self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.filter(title='New Book').count(), 1)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        url = reverse('book-create')
        data = {'title': 'Unauthorized Book', 'publication_year': 2023, 'author': self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------ Filtering / Searching / Ordering ------------------

    def test_filter_by_title(self):
        url = reverse('book-list') + '?title=1984'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_search_by_author(self):
        url = reverse('book-list') + '?search=Rowling'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['author'], self.author2.id)

    def test_ordering_by_publication_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))
