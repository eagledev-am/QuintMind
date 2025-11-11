from django.db import models
from django.conf import settings

class Author(models.Model):
    """Stores information about a book's author."""
    name = models.CharField(max_length=255)
    Bio = models.TextField(blank=True, null=True)
    DateOfBirth = models.DateField(blank=True, null=True)
    Photo = models.ImageField(upload_to='author_photos/', blank=True, null=True)
    Nationality = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Stores book categories or genres (e.g., Fantasy, Sci-Fi)."""
    Tag = models.CharField(max_length=100, unique=True)
    Description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.Tag


class Book(models.Model):
    """The main Book model."""
    title = models.CharField(max_length=255)
    Description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    Edition = models.CharField(max_length=100, blank=True, null=True)
    NumberOfPages = models.PositiveIntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Language = models.CharField(max_length=50, blank=True, null=True)
    PublishDate = models.DateField(blank=True, null=True)

    
    authors = models.ManyToManyField(Author, related_name='books')
    
    
    categories = models.ManyToManyField(Category, related_name='books')
    
    
    ebook_content_url = models.FileField(upload_to='ebooks/', blank=True, null=True)
    
    def __str__(self):
        return self.title


class UserRating(models.Model):
    """
    Junction table for User and Book, storing the rating.
    We need this as a manual table to store 'rating_value'.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    rating_value = models.PositiveSmallIntegerField() # e.g., 1 to 5
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book') 

    def __str__(self):
        return f"{self.user.email} rates {self.book.title}: {self.rating_value}"


class UserReadingProgress(models.Model):
    """
    Junction table for User and Book, storing e-reader progress.
    This is for the subscription feature.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reading_progress')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reading_progress')
    current_page = models.PositiveIntegerField(default=0)
    last_read_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.email} is on page {self.current_page} of {self.book.title}"