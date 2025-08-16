from rest_framework import serializers
from .models import Level, Lesson
from .models import UserProgress
from .models import SpeakingFeedback

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

# Liste görünümü için sade/okunaklı serializer
class LessonListSerializer(serializers.ModelSerializer):
    level = serializers.StringRelatedField()  # "A1", "A2" gibi düz metin

    class Meta:
        model = Lesson
        fields = ("id", "title", "level", "audio_url", "transcript")

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'        

class SpeakingFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingFeedback
        fields = '__all__'
        read_only_fields = ['user']