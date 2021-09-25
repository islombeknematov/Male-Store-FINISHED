from django.contrib import admin

# Register your models here.
from blog.models import AuthorModel, PostTagModel, PostModel, CommentModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['full_name']


@admin.register(PostTagModel)
class PostTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']



@admin.register(PostModel)
class PostModeladmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    list_filter = ['author', 'tags', 'created_at']
    search_fields = ['title']
    autocomplete_fields = ['author', 'tags']



@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_diplay = ['name', 'email', 'phone', 'created_at']
    list_filter = ['created_at']

