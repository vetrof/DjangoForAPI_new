from django.shortcuts import render
from rest_framework import generics

from api.serializers import BookSerializer
from books.models import Book


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
