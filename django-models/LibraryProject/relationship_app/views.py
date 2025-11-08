from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library


def list_books(request):
    """Function-based view that lists all books."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """Class-based view that displays details for a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'