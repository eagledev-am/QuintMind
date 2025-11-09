from django.db import models
from django.conf import settings

class DiscussionRoom(models.Model):
    """
    A 1-to-1 container for all posts related to a single book.
    """
    # OneToOneField enforces the 1-to-1 relationship from our schema
    book = models.OneToOneField('books.Book', on_delete=models.CASCADE, related_name='discussion_room')
    room_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_name


class Post(models.Model):
    """
    A single post (topic) within a DiscussionRoom, created by a User.
    """
    room = models.ForeignKey(DiscussionRoom, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    """
    A reply to a Post, written by a User.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # This enables threaded comments
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"Comment by {self.user.email} on {self.post.post_title}"


class PostLike(models.Model):
    """
    Junction table for Users liking Posts.
    We make this manually to store the 'created_at' timestamp.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post') # User can only like a post once

    def __str__(self):
        return f"{self.user.email} likes {self.post.post_title}"