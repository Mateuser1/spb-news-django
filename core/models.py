from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    work = models.CharField(max_length=100, verbose_name='Работа')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    content = models.TextField(verbose_name='Текст статьи')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title