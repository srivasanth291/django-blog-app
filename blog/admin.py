from django.contrib import admin
from .models import BlogPost, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_name', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'content', 'author_name')
