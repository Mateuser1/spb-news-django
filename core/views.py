from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import Article
from core.serializers import ArticleSerializer


# Create your views here.

class ArticleView(viewsets.ModelViewSet):
    queryset: QuerySet[Article] = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=['get'], detail=False)
    def get_articles(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
