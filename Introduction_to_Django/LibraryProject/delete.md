from bookshelf.models import Book

# Get the book using get()
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()

# Verify deletion: try to list all books
Book.objects.all()
# <QuerySet []>
