from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    LevelListAPIView,
    UserProgressListCreateView,
    UserProgressDetailView,
    LessonViewSet
)


# Router tanımı
router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lesson')

# Sadece level için manuel endpoint
urlpatterns = [
    path('levels/', LevelListAPIView.as_view(), name='level-list'),
    path('progress/', UserProgressListCreateView.as_view(), name='progress-list-create'),
    path('progress/<int:pk>/', UserProgressDetailView.as_view(), name='progress-detail'),
]

# Router URL'lerini ekliyoruz
urlpatterns += router.urls

