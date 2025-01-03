from django.shortcuts import render

def homepage(request):
    return render(request, "templates/home.html")

def books_index(request):
    return render(request, "templates/book_index.html")
