from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Category, Book, UserRating, UserReadingProgress
from .serializers import (
    AuthorSerializer, 
    CategorySerializer, 
    BookSerializer, 
    UserRatingSerializer, 
    UserReadingProgressSerializer
)
from .filters import BookFilter # <-- Importing our new filter

# --- Custom Permissions ---

class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_staff

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        return obj.user == request.user



class AuthorListCreateView(generics.ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend] 
    filterset_class = BookFilter          

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]



class UserRatingListCreateView(generics.ListCreateAPIView):
    serializer_class = UserRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return UserRating.objects.filter(user=self.request.user)
    

class UserRatingDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserRatingSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner] # Must be owner

    def get_queryset(self):
        return UserRating.objects.filter(user=self.request.user)

class UserReadingProgressListCreateView(generics.ListCreateAPIView):

    serializer_class = UserReadingProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserReadingProgress.objects.filter(user=self.request.user)

class UserReadingProgressDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserReadingProgressSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner] # Must be owner

    def get_queryset(self):

        return UserReadingProgress.objects.filter(user=self.request.user)