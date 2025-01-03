from django.shortcuts import render

from books.models import Book

def homepage(request):
    return render(request, "templates/home.html")

def books_index(request):
    available_books = Book.objects.all()

    return render(request, "templates/book_index.html", {"books": available_books})
