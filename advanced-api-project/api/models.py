from django.db import models

# Author model:
# Holds basic information about book authors.
# One author can have many books (One-to-Many).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model:
# Stores details for each book and links to its author.
# author = ForeignKey → establishes One Author → Many Books
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',      # used to access books from AuthorSerializer
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

