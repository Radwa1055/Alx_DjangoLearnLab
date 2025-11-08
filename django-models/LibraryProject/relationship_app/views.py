from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


def list_books(request):
    books = Book.objects.all()
    
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
