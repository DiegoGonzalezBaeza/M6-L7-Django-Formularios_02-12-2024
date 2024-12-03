from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, LibraryForm, SectionForm
from .models import Author, Book, Library, Section

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'form/author_form.html', {'form': form})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'form/author_list.html', {'authors': authors})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'form/book_form.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'form/book_list.html', {'books': books})


def library_create(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library_list')
    else:
        form = LibraryForm()
    return render(request, 'form/library_form.html', {'form': form})

def library_list(request):
    library = Library.objects.all()
    return render(request, 'form/library_list.html', {'libraries': library})




def section_create(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = SectionForm()
    return render(request, 'form/section_form.html', {'form': form})


def section_list(request):
    section = Section.objects.all()
    return render(request, 'form/section_list.html', {'sections': section})