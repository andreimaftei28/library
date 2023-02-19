from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer): 
    subject = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()
  
    class Meta:
        model = Book
        fields = ('name', 'isbn', 'image', 'preview', 'subject', 'author', 'publisher')