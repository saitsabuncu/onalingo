from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LessonViewSet, LevelListAPIView

# Router tanımı
router = DefaultRouter()
router.register(r'lessons', LessonViewSet, basename='lesson')

# Sadece level için manuel endpoint
urlpatterns = [
    path('levels/', LevelListAPIView.as_view(), name='level-list'),
]

# Router URL'lerini ekliyoruz
urlpatterns += router.urls

