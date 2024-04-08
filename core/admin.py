from django.contrib import admin

from core.models import Author, Article


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)