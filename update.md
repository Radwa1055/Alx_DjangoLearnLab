# Test 3: Update the book
book.title = "Updated Book"
book.save()
updated = Book.objects.get(id=book.id)
assert updated.title == "Updated Book", "Book was not updated"
print("✓ Update test passed")

