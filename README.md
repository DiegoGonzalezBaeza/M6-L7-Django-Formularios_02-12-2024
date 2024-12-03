# M6-L7-Django-Formularios_02-12-2024

# Django Form Handling Project

Este proyecto es una aplicación básica de Django que implementa la creación y visualización de autores, libros y bibliotecas utilizando formularios, modelos y vistas.

## Características

- **Modelos:** 
  - `Author`: Representa a los autores con un campo `name`.
  - `Book`: Representa libros con un campo `title` y una relación de clave foránea hacia `Author`.
  - `Library`: Representa bibliteca con un campo `name`, `anio` y una relación de clave foránea hacia `Book`.

- **Formularios:** 
  - `AuthorForm`: Maneja la creación y edición de autores.
  - `BookForm`: Maneja la creación y edición de libros.
  - `LibraryForm`: Maneja la creación y edición de bibliotecas.

- **Vistas:** 
  - `author_create`: Crea nuevos autores.
  - `author_list`: Muestra la lista de autores.
  - `book_create`: Crea nuevos libros.
  - `book_list`: Muestra la lista de libros.
  - `library_create`: Crea nuevas bibliotecas.
  - `library_list`: Muestra la lista de bibliotecas.

- **Admin:** Configurado para registrar y administrar los modelos `Author`, `Book` y `Library`.

## Estructura de URLs

- `/authors/`: Lista de autores.
- `/authors/new/`: Formulario para crear un nuevo autor.
- `/books/`: Lista de libros.
- `/books/new/`: Formulario para crear un nuevo libro.
- `/libraries/`: Lista de bibliotecas.
- `/libraries/new/`: Formulario para crear un nueva biblioteca.

## Requisitos

- Python 3.x
- Django >= 4.0

## Instalación y Configuración

1. Clonar el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd form_handling_project
   ```

2. Crear un entorno virtual y activarlo:
   ```bash
   python -m venv env
   source env/bin/activate # En Windows: env\Scripts\activate
   ```

3. Instalar las dependencias:
   ```bash
   pip install django
   ```

4. Ejecutar migraciones:
   ```bash
   python manage.py migrate
   ```

5. Crear un superusuario (opcional para acceso al admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

7. Abrir en el navegador:
   - [http://127.0.0.1:8000/authors/](http://127.0.0.1:8000/authors/)
   - [http://127.0.0.1:8000/books/](http://127.0.0.1:8000/books/)

## Archivos Clave

### **`models.py`**
Define los modelos `Author`, `Book` y `Library`:

```python
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
```

### **`forms.py`**
Define los formularios `AuthorForm` y `BookForm`:

```python
from django import forms
from .models import Author, Book, Library

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
```

### **`views.py`**
Contiene las vistas para manejar autores y libros:

```python
from django.shortcuts import render, redirect
from .forms import AuthorForm, BookForm, LibraryForm
from .models import Author, Book, Library

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
    return render(request, 'form/library_list.html', {'library': library})
```

### **`urls.py`**
Define las rutas de la aplicación:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/new/', views.author_create, name='author_create'),

    path('books/', views.book_list, name='book_list'),
    path('books/new/', views.book_create, name='book_create'),

    path('libraries/', views.library_list, name='library_list'),
    path('libraries/new/', views.library_create, name='library_create'),
]
```

### **`admin.py`**
Registra los modelos en el panel de administración:

```python
from django.contrib import admin
from .models import Author, Book, Library

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
```

## Plantillas

- **`author_list.html`**: Lista los autores.
- **`author_form.html`**: Formulario para crear autores.
- **`book_list.html`**: Lista los libros.
- **`book_form.html`**: Formulario para crear libros.
- **`library_list.html`**: Lista los libros.
- **`library_form.html`**: Formulario para crear libros.