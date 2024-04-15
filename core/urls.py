from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import ArticleView, AuthorView

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('all/', ArticleView.as_view({'get': 'get_articles'})),
    path('all/', AuthorView.as_view({'get': 'get_authors'})),
]
