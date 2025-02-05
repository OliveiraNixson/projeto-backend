from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    biography = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title