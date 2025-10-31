### Delete the Book instance using get() then delete()

from bookshelf.models import Book

# Get the book using get()
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()

# Verify deletion: list all books
Book.objects.all()
# <QuerySet []>
