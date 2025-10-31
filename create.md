from bookshelf.models import Book

# Test 1: Create a book
book = Book.objects.create(title="Test Book", author="Test Author", publication_year=2024)
assert book.id is not None, "Book was not created"
print("✓ Create test passed")