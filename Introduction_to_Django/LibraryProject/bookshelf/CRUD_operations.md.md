# CREATE
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
<Book: 1984>

# RETRIEVE
>>> Book.objects.all()
<QuerySet [<Book: 1984>]>

# UPDATE
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
<Book: Nineteen Eighty-Four>

# DELETE
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
