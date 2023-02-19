from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.db.models import Count

from .models import CustomAddress, Author, Publisher, Subject, Book


# Register your models here.
@admin.register(CustomAddress)
class CustomAddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "view_same_author_link")
    
    def view_same_author_link(self, obj):
        # TODO: fix filter by author
        
        count = Book.objects.filter(author=obj).aggregate(Count("name"))
        
        url = (
            reverse("admin:books_book_changelist")
            + "?"
            + urlencode({"book__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Books</a>', url, count["name__count"])

    view_same_author_link.short_description = "Books"
    
    
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "address")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "isbn", "same_author")
    list_filter = ("author",)
    def same_author(self, obj):
       
        result = Author.objects.filter(name=obj.author).aggregate(Count("name"))
        return result["name__count"]