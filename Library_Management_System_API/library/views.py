from rest_framework.viewsets import ModelViewSet
from .models import Book, BookCheckout
from .serializers import BookSerializer, BookCheckoutSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from rest_framework.generics import ListAPIView
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Library Management System!")

# Book ViewSet to handle book operations:
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'title'


# BookCheckout View to handle book checkout and return operations:
class CheckOutBookView(APIView):

    permission_classes = [IsAuthenticated]
    def post(self, request):
        """
        Checks out a book for the current user.

        Args:
            request: The request object with the book_id as a parameter.

        Returns:
            A response object with a message or an error if the book is already checked out or unavailable.
        """
        user = request.user
        book_id = request.data.get('book_id')
        book = get_object_or_404(Book, pk=book_id)

        # Check if the user already checked out this book
        if BookCheckout.objects.filter(user=user, book=book, return_date__isnull=True).exists():
            return Response({"error": "You already have this book checked out."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if there are available copies
        if book.number_of_copies < 1:
            return Response({"error": "No copies available for this book."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a checkout record
        BookCheckout.objects.create(user=user, book=book)
        book.number_of_copies -= 1
        book.save()

        return Response({"message": f"You have successfully checked out '{book.title}'."}, status=status.HTTP_200_OK)


# BookReturn View to handle book return operations:
class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        """
        Returns a book for the current user.

        Args:
            request: The request object with the book_id as a parameter.

        Returns:
            A response object with a message or an error if the book is not checked out by the user.
        """

        user = request.user
        book_id = request.data.get('book_id')
        book = get_object_or_404(Book, id=book_id)

        # Get the checkout record
        checkout = BookCheckout.objects.filter(user=user, book=book, return_date__isnull=True).first()
        if not checkout:
            return Response({"error": "You don't have this book checked out."}, status=status.HTTP_400_BAD_REQUEST)

        # Update the checkout record
        checkout.return_date = now()
        checkout.save()

        # Increase available copies
        book.number_of_copies += 1
        book.save()

        return Response({"message": f"You have successfully returned '{book.title}'."}, status=status.HTTP_200_OK)


# AvailableBooksView to handle available book operations:
class AvailableBooksView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        """
        Returns a queryset of books that are available, filtered by title, author, or ISBN if provided in the query parameters.

        :return: A queryset of books that are available
        """
        queryset = super().get_queryset()

         # Filter by availability
        available = self.request.query_params.get('available')
        if available == 'true':
            queryset = queryset.filter(number_of_copies__gt=0)

        # Filter by title, author, or ISBN
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        isbn = self.request.query_params.get('isbn')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if isbn:
            queryset = queryset.filter(isbn__icontains=isbn)
        if title and author and isbn:
            queryset = queryset.filter(title__icontains=title, author__icontains=author, isbn__icontains=isbn)

        return queryset