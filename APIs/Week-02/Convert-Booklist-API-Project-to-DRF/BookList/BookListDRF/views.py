from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Book
from .serializars import BookSerializer


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
