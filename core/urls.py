from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import ArticleView, AuthorView

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),

    # ARTICLE
    path('article/all/', ArticleView.as_view({'get': 'get_articles'})),
    path('article/create/', ArticleView.as_view({'post': 'create_article'})),
    path('article/delete/', ArticleView.as_view({'delete': 'delete_article'})),
    path('article/update/', ArticleView.as_view({'put': 'update_article'})),

    # AUTHOR
    path('author/all/', AuthorView.as_view({'get': 'get_authors'})),
    path('author/create/', AuthorView.as_view({'post': 'create_author'})),
    path('author/delete/', AuthorView.as_view({'delete': 'delete_author'})),
]
