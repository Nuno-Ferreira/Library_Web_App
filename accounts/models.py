from django.db import models
from django.contrib.auth.models import User

from books.models import Book

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username

    @property
    def books(self):
        return Book.objects.filter(user=self.user)
