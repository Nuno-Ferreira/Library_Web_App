from django.shortcuts import render

from books.models import Book

def homepage(request):
    return render(request, "templates/home.html")

def books_index(request):
    available_books = Book.objects.all()

    return render(request, "templates/book_index.html", {"books": available_books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)

    return render(request, "templates/book_detail.html", {"book": book})
