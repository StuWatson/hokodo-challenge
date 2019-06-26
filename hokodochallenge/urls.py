"""hokodochallenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.urls import path
from .books.views import ListBooks, ListAuthors

urlpatterns = [
    path('books', ListBooks.as_view(), name='books'),
    path('authors', ListAuthors.as_view(), name='authors')
]
