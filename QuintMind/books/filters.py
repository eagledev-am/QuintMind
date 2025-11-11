from django_filters import rest_framework as filters
from .models import Book, Author, Category

class BookFilter(filters.FilterSet):

    
    # Allows partial, case-insensitive search for title
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    
    # Allows filtering by author's name
    author_name = filters.CharFilter(field_name='authors__name', lookup_expr='icontains')
    
    # Allows filtering by category tag
    category_tag = filters.CharFilter(field_name='categories__Tag', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author_name', 'category_tag', 'Language']