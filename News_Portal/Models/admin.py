from django.contrib import admin

from .models import Author, Category, Post, Comment, PostCategory

class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'post_time', 'rating')
    list_filter = ('author', 'post_time', 'rating')

admin.site.register(Post, PostsAdmin)

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostCategory)


