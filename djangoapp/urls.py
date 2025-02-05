from django.urls import path
from .views import BookListCreate, BookDetail, AuthorListCreate, AuthorDetail

urlpatterns = [
    path('api/books/', BookListCreate.as_view(), name='book-list'),
    path('api/books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('api/authors/', AuthorListCreate.as_view(), name='author-list'),
    path('api/authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
]