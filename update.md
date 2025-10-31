from bookshelf.models import Book

# Get the existing book using get()
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update using get() again
updated = Book.objects.get(pk=book.pk)
updated.title
# "Nineteen Eighty-Four"

# Or show all objects
Book.objects.all()
# <QuerySet [<Book: Nineteen Eighty-Four>]>

