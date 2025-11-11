from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [
    # /api/v1/books/authors/
    path('authors/', views.AuthorListCreateView.as_view(), name='author-list'),
    
    # /api/v1/books/authors/1/
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    
    # /api/v1/books/categories/
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    
    # /api/v1/books/categories/1/
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    
    # /api/v1/books/
    path('', views.BookListCreateView.as_view(), name='book-list'),
    
    # /api/v1/books/1/
    path('<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    
    # /api/v1/books/ratings/ (Lists *your* ratings, or creates a new one)
    path('ratings/', views.UserRatingListCreateView.as_view(), name='rating-list'),
    
    # /api/v1/books/ratings/1/ (Updates/deletes *your* rating)
    path('ratings/<int:pk>/', views.UserRatingDetailView.as_view(), name='rating-detail'),
    
    # /api/v1/books/progress/ (Lists *your* progress, or creates/updates it)
    path('progress/', views.UserReadingProgressListCreateView.as_view(), name='progress-list'),
    
    # /api/v1/books/progress/1/ (Updates/deletes *your* progress record)
    path('progress/<int:pk>/', views.UserReadingProgressDetailView.as_view(), name='progress-detail'),
]