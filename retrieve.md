# Test 2: Retrieve the book
retrieved = Book.objects.get(id=book.id)
assert retrieved.title == "Test Book", "Book was not retrieved correctly"
print("✓ Retrieve test passed")

