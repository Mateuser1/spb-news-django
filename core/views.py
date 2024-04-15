from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from core.models import Article, Author
from core.serializers import ArticleSerializer, AuthorSerializer


# Create your views here.

class ArticleView(viewsets.ModelViewSet):
    queryset: QuerySet[Article] = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def get_articles(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def create_article(self, request):
        data = request.data
        author = get_object_or_404(Author, pk=data['author'])
        article = Article.objects.create(
            title=data['title'],
            content=data['content'],
            author=author,
        )
        serializer = self.serializer_class(article)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AuthorView(viewsets.ModelViewSet):
    queryset: QuerySet[Author] = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def get_authors(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
