from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, User. You're at the books index.")
