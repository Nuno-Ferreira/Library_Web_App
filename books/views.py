from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, "templates/home.html")

def index(request):
    return HttpResponse("Hello, User. You're at the books index.")
