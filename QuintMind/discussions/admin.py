from django.contrib import admin

from .models import DiscussionRoom, Post , Comment, PostLike


@admin.register(DiscussionRoom)
class DiscussionRoomAdmin(admin.ModelAdmin):
    list_display = ('room_name', 'book', 'created_at')
    search_fields = ('room_name', 'book__title')
    ordering = ('created_at',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'room', 'user', 'created_at')
    search_fields = ('post_title', 'user__email')
    ordering = ('created_at',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'created_at')
    search_fields = ('user__email', 'post__post_title')
    ordering = ('created_at',)

@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    search_fields = ('user__email', 'post__post_title')
    ordering = ('created_at',)