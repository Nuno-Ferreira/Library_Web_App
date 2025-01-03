from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="HomePage"),
    path("books/", views.books_index, name="BooksIndex"),
    path("books/<int:book_id>/", views.book_detail, name="BookDetail"),
]
