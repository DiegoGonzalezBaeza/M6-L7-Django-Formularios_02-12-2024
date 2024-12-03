from django import forms
from .models import Author, Book, Library, Section

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'