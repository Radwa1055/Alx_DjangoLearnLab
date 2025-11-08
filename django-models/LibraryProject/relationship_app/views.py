from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library 
from .models import Book     

# Function-based view
def list_books(request):
    books = Book.objects.all()
    if request.GET.get('format') == 'txt':
        output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
        return HttpResponse(output, content_type="text/plain")
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ✅ Class-based view for Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
