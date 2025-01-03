from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="HomePage"),
    path("books/", views.books_index, name="BooksIndex"),
]
