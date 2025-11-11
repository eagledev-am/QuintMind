from rest_framework import serializers
from .models import Author, Category, Book, UserRating, UserReadingProgress
from django.conf import settings
from django.db.models import Avg

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'Bio', 'DateOfBirth', 'Photo', 'Nationality']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'Tag', 'Description']

class BookSerializer(serializers.ModelSerializer):
    # The stringRelatedField will return a list of human-readable strings
    # StringRelatedField simply calls the __str__() method of each related object.
    authors = serializers.StringRelatedField(many=True, read_only=True)
    categories = serializers.StringRelatedField(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField(read_only=True)

    # --- WRITE-ONLY FIELDS ---
    author_ids = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), 
        many=True, 
        write_only=True, 
        source='authors' 
    )
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), 
        many=True, 
        write_only=True, 
        source='categories' 
    )
    class Meta:
        model = Book
        fields = [
            'id', 
            'title', 
            'Description', 
            'cover_image',
            'Edition', 
            'NumberOfPages', 
            'Price', 
            'Language', 
            'PublishDate',
            'ebook_content_url', 
            'authors',           
            'categories',
            'average_rating',
            'author_ids',
            'category_ids',
        ]
    def get_average_rating(self, obj):
        avg = obj.ratings.aggregate(Avg('rating_value'))['rating_value__avg']
        if avg is None:
            return 0.0
        return round(avg, 1) # Round to one decimal place
class UserRatingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserRating
        fields = [
            'user', 
            'book', 
            'rating_value', 
            'created_at'
        ]
        read_only_fields = ['created_at']
    
    def validate_rating_value(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
    
class UserReadingProgressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserReadingProgress
        fields = [
            'user', 
            'book', 
            'current_page', 
            'last_read_timestamp'
        ]
        read_only_fields = ['last_read_timestamp']