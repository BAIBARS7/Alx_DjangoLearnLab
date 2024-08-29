from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


class BookList(rest_framework.generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
