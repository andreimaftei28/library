from django.urls import path
from .views import BookAPIView, BookDetailAPIView

urlpatterns = [
    path("<int:pk>/", BookDetailAPIView.as_view(), name="book_detail"),
    path("", BookAPIView.as_view(), name="books"),
]
