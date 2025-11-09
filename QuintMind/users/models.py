from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True)
    Bio = models.TextField(blank=True, null=True)
    Photo = models.ImageField(upload_to='user_photos/', blank=True, null=True)
    DateOfBirth = models.DateField(blank=True, null=True)
    Nationality = models.CharField(max_length=100, blank=True, null=True)
    
    role = models.CharField(max_length=50, default='user')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class UserContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    contact_type = models.CharField(max_length=50) # e.g., 'Website', 'Twitter'
    contact_value = models.CharField(max_length=255) # e.g., 'https://myblog.com'

    class Meta:
        unique_together = ('user', 'contact_type') 

    def __str__(self):
        return f"{self.user.email} - {self.contact_type}"


class UserFollowsAuthor(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_authors')
    
    author = models.ForeignKey('books.Author', on_delete=models.CASCADE, related_name='followers')
    
    class Meta:
        unique_together = ('user', 'author') # Ensures a user can't follow the same author twice

    def __str__(self):
        return f"{self.user.email} follows {self.author.name}"