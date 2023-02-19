from django.shortcuts import render
from django.urls import reverse_lazy as r
from django.views.generic import ListView, CreateView

from .models import Book
from .forms import BookForm


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"

class BookCreate(CreateView):
    template_name = 'add_book_form.html'
    model = Book
    form_class = BookForm
    success_url = r('home')
