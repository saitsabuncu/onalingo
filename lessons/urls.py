from django.urls import path
from .views import LevelListAPIView, LessonListAPIView, LessonDetailAPIView

urlpatterns = [
    path('levels/', LevelListAPIView.as_view(), name='level-list'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:id>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
]
