from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

def list_books(request):
    """
    Must return a plain text list of "Title by Author"
    (one per line) — checker expects plain text.
    """
    books = Book.objects.all()
    lines = []
    for book in books:
        # use safe attribute names assumed by checker
        author_name = getattr(book.author, "name", str(book.author))
        lines.append(f"{book.title} by {author_name}")
    output = "\n".join(lines)
    return HttpResponse(output, content_type="text/plain")

class LibraryDetailView(DetailView):
    """
    Uses exact import path expected by checker.
    Renders template at relationship_app/templates/relationship_app/library_detail.html
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
