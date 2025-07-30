from rest_framework import serializers
from .models import Level, Lesson
from .models import UserProgress
from .models import SpeakingFeedback

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    level = LevelSerializer()  # İlgili seviyeyi de içersin

    class Meta:
        model = Lesson
        fields = '__all__'

class UserProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProgress
        fields = '__all__'        

class SpeakingFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingFeedback
        fields = '__all__'
        read_only_fields = ['user']