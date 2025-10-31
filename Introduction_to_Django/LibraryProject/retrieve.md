>>> from bookshelf.models import Book
>>> books = Book.objects.all()
>>> books
<QuerySet [<Book: 1984>]>
>>> books[0].title
'1984'
>>> books[0].author
'George Orwell'
>>> books[0].publication_year
1949
