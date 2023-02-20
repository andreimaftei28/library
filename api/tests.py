from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from books.models import Book, Author, Subject, Publisher


class APITests(APITestCase):
    
    
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
        name="Ammaniti",
        isbn="1234567890123",
        image=SimpleUploadedFile(name="test_image.jpg", content=open("C:\\Users\\andre\Desktop\\book_library\\library\\media\\static\\images\\test_image.jpg", 'rb').read(), content_type='image/jpeg'),
        preview=SimpleUploadedFile(name="test_file.pdf", content=open("C:\\Users\\andre\Desktop\\book_library\\library\\media\\static\\previews\\test_file.pdf", 'rb').read(), content_type='application/pdf'),
        subject=Subject.objects.create(name="Storie adolescentine"),
        
        author=Author.objects.create(name="Niccolò Ammaniti"),   
        publisher=Publisher.objects.create(name="Sergio Albelli")
        )
    
    
    def test_api_listview(self):
        response = self.client.get(reverse("books"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)

