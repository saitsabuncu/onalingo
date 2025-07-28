from rest_framework import viewsets
from .models import Lesson, Level
from .serializers import LessonSerializer, LevelSerializer
from .permissions import IsAdminOrReadOnly

# Level listesi sadece GET olacak şekilde bırakılabilir
from rest_framework import generics

class LevelListAPIView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

# Ders CRUD işlemleri için ViewSet kullanalım
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminOrReadOnly]
