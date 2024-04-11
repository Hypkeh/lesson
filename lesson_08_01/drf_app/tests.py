from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse_lazy

from .models import Author, Book

# Create your tests here.


class BookTests(APITestCase):

    def setUp(self) -> None:
        self.author = Author.objects.create(name='author_1')

        self.book_data = {
            'title': 'test_book',
            "description": "test_description",
            'author': {"name": self.author.name}
        }

        self.list_url = reverse_lazy('book_list')
        self.detail_url = reverse_lazy('book_detail')

    def test_create_book(self):

        response = self.client.post(self.list_url, self.book_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.first().title, self.book_data['title'])

    def test_list_book(self):
        book1 = Book.objects.create(title='book1', author=self.author)
        book2 = Book.objects.create(title='book2', author=self.author)

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_detail_book(self):
        book = Book.objects.create(title='detail book', author=self.author, description="Test description")
        url_detail = reverse_lazy('book_detail', args=[book.pk])

        response = self.client.get(url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], book.title)

    def test_update_book(self):
        book = Book.objects.create(title='detail book', author=self.author, description="Test description")
        url_detail = reverse_lazy('book_detail', args=[book.pk])
        updated_data = {'title': 'updated_title', 'author': {"name": "new_author_name"}, "description": "description_test"}

        response = self.client.put(url_detail, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        book.refresh_from_db()
        self.assertEqual(book.title, updated_data['title'])

    def test_delete_book(self):
        book = Book.objects.create(title="book to be deleted", author=self.author, description="Test description")
        url_detail = reverse_lazy('book_detail', args=[book.pk])

        response = self.client.delete(url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=book.pk).exists())

