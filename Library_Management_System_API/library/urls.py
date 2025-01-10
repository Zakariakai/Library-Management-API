from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CheckOutBookView, ReturnBookView, AvailableBooksView
from django.urls import path

# Defining the URL patterns for the book viewset
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Defining the URL patterns for the checkout and return views
urlpatterns = [
    path('books/checkout/', CheckOutBookView.as_view(), name='checkout-book'),
    path('books/return/', ReturnBookView.as_view(), name='return-book'),
    path('available-books/', AvailableBooksView.as_view(), name='available-books'),
]

# Adding the router URLs
urlpatterns += router.urls
