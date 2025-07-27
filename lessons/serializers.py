from rest_framework import serializers
from .models import Level, Lesson

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    level = LevelSerializer()  # İlgili seviyeyi de içersin

    class Meta:
        model = Lesson
        fields = '__all__'
