from django.contrib import admin
from .models import CustomAddress, Author, Publisher, Subject, Book


# Register your models here.
@admin.register(CustomAddress)
class CustomAddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "address")

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "isbn", "same_author")
    
    def same_author(self, obj):
        from django.db.models import Count
        result = Author.objects.filter(name=obj.author).aggregate(Count("name"))
        return result["name__count"]