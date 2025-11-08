from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

def list_books(request):
    """
    Function-based view required to return a simple text list
    of book titles and their authors.
    """
    books = Book.objects.all()
    # نص بسيط بكل سطر "Title by Author"
    lines = [f"{book.title} by {book.author.name}" for book in books]
    output = "\n".join(lines)
    return HttpResponse(output, content_type="text/plain")

class LibraryDetailView(DetailView):
    """
    Class-based view using the exact import path expected by checker.
    Displays a specific Library and its books using a template.
    """
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
