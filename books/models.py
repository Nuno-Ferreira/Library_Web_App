from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey("accounts.UserProfile", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
