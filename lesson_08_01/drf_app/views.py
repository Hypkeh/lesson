from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
# Create your views here.

@api_view(['GET'])
def authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


def spa(request):
    return render(request, 'drf_app/spa.html')
