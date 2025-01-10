from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

#book model:
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    number_of_copies = models.PositiveIntegerField()
    def __str__(self):
        """
        Returns a string representation of the Book model instance, which is the title of the book.
        """
        return self.title

# book checkout model:
class BookCheckout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """
        Returns a string representation of the BookCheckout model instance, which is the username of the user
        who checked out the book and the title of the book.
        """
        return f"{self.user.username} - {self.book.title}"        