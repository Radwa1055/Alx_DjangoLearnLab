book.delete()
assert Book.objects.filter(id=book.id).count() == 0, "Book was not deleted"
print("✓ Delete test passed")

print("\n✓ All tests passed!")