# CREATE
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# RETRIEVE
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")

# UPDATE
book.title = "Nineteen Eighty-Four"
book.save()
print(book)

# DELETE
book.delete()
print(Book.objects.all())