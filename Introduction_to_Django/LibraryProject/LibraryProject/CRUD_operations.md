from bookshelf.models import Book

# Test 1: Create a book
book = Book.objects.create(title="Test Book", author="Test Author", publication_year=2024)
assert book.id is not None, "Book was not created"
print("✓ Create test passed")

# Test 2: Retrieve the book
retrieved = Book.objects.get(id=book.id)
assert retrieved.title == "Test Book", "Book was not retrieved correctly"
print("✓ Retrieve test passed")

# Test 3: Update the book
book.title = "Updated Book"
book.save()
updated = Book.objects.get(id=book.id)
assert updated.title == "Updated Book", "Book was not updated"
print("✓ Update test passed")

# Test 4: Delete the book
book.delete()
assert Book.objects.filter(id=book.id).count() == 0, "Book was not deleted"
print("✓ Delete test passed")

print("\n✓ All tests passed!")