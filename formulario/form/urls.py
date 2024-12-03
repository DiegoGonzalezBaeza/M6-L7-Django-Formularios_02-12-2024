from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/new/', views.author_create, name='author_create'),

    path('books/', views.book_list, name='book_list'),
    path('books/new/', views.book_create, name='book_create'),

    path('libraries/', views.library_list, name='library_list'),
    path('libraries/new/', views.library_create, name='library_create'),

    path('sections/', views.section_list, name='section_list'),
    path('sections/new/', views.section_create, name='section_create'),
]