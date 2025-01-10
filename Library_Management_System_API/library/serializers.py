from rest_framework import serializers
from library.models import Book, BookCheckout

# Book Serializer to handle data conversion:
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Book Checkout Serializer to handle data conversion:
class BookCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCheckout
        fields = ['id', 'user', 'book', 'checkout_date', 'return_date']
        read_only_fields = ['checkout_date', 'return_date']
