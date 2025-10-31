### Retrieve the created Book using get()

from bookshelf.models import Book

# Retrieve the book we created using get (by title)
book = Book.objects.get(title="1984")

# Display all attributes
book.title
# "1984"
book.author
# "George Orwell"
book.publication_year
# 1949

# Show the object
book
# <Book: 1984>

