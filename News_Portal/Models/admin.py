from django.contrib import admin
from .models import Author, Category, Post, Comment, PostCategory
from modeltranslation.admin import TranslationAdmin # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)

class PostsAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'post_time', 'rating')
    list_filter = ('author', 'post_time', 'rating')

# Регистрируем модели для перевода в админке
class PostAdmin(TranslationAdmin):
    model = Post
  
class CommentAdmin(TranslationAdmin):
    model = Comment

admin.site.register(Post, PostsAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostCategory)


