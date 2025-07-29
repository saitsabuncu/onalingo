from rest_framework import viewsets, generics, permissions
from .models import Lesson, Level, UserProgress
from .serializers import LessonSerializer, LevelSerializer, UserProgressSerializer
from .permissions import IsAdminOrReadOnly

class LevelListAPIView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAdminOrReadOnly]

class UserProgressListCreateView(generics.ListCreateAPIView):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProgressDetailView(generics.RetrieveUpdateAPIView):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
