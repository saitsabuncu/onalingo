from rest_framework import viewsets, generics, permissions
from .models import Lesson, Level, UserProgress
from .serializers import LessonSerializer, LevelSerializer, UserProgressSerializer
from .permissions import IsAdminOrReadOnly
from .models import SpeakingFeedback
from .serializers import SpeakingFeedbackSerializer
from .serializers import LessonListSerializer


class LevelListAPIView(generics.ListAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        # /api/lessons/ -> list
        if getattr(self, "action", None) == "list":
            return LessonListSerializer
        return LessonSerializer


class UserProgressListCreateView(generics.ListCreateAPIView):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProgressDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        return UserProgress.objects.filter(user=self.request.user)
    
class SpeakingFeedbackListCreateView(generics.ListCreateAPIView):
    serializer_class = SpeakingFeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SpeakingFeedback.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)