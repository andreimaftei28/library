from django.contrib import admin
from .models import CustomAddress, Author, Publisher, Subject, Book


# Register your models here.
admin.site.register(CustomAddress)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Subject)
admin.site.register(Book)
