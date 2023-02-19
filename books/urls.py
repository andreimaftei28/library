from django.urls import path

from .views import BookListView, BookCreate

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path("add/", BookCreate.as_view(), name="book_add"),
]