from django.contrib import admin

# Register your models here.
from .models import Author, Book, Library, Section

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Section)