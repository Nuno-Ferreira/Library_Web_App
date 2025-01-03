from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import UserProfile
from books.models import Book

def homepage(request):
    users = UserProfile.objects.order_by("user__username")[:3]
    books = Book.objects.filter(user=None)[:3]
    
    return render(request, "templates/home.html", {"user_profiles": users, "books": books})

def books_index(request):
    available_books = Book.objects.filter(user=None)

    return render(request, "templates/book_index.html", {"books": available_books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)

    return render(request, "templates/book_detail.html", {"book": book})

@login_required
def assign_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if not book.user:
        book.user = user_profile
        book.save()

    return render(request, "templates/book_detail.html", {"book": book})
