from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for Book model:
# Includes custom validation to prevent future publication years.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation:
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author model:
# Includes nested BookSerializer to return all books of the author.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to show all related books automatically
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
