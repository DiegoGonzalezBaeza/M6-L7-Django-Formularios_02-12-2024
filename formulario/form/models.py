from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    anio = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Section(models.Model):
    
    FANTASY = 'Fantasy'
    HISTORY = 'History'
    POLITIC = 'Politic'
    SCIENCE_FICTION = 'Science Fiction'

    CATEGORY_CHOICES = [
        (FANTASY, 'Fantasy'),
        (HISTORY, 'History'),
        (POLITIC, 'Politic'),
        (SCIENCE_FICTION, 'Science Fiction'),
    ]

    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.category