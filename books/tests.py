from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Book, Author, Subject, Publisher

# Create your tests here.
class BookTests(TestCase):
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
        
        print(cls.book.subject)

    def test_book_content(self):
        self.assertEqual(self.book.name, "Ammaniti")
        self.assertEqual(self.book.isbn, "1234567890123")
        self.assertEqual(Subject.objects.last().name, "Storie adolescentine")
        self.assertEqual(Author.objects.last().name, "Niccolò Ammaniti")
        self.assertEqual(Publisher.objects.last().name, "Sergio Albelli")
        
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ammaniti")
        self.assertTemplateUsed(response, "book_list.html")