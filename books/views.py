from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from books.models import Book

def homepage(request):
    return render(request, "templates/home.html")

def books_index(request):
    available_books = Book.objects.filter(user=None)

    return render(request, "templates/book_index.html", {"books": available_books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)

    return render(request, "templates/book_detail.html", {"book": book})

@login_required
def assign_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if not book.user:
        book.user = request.user
        book.save()

    return render(request, "templates/book_detail.html", {"book": book})
