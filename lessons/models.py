from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=20)  # A1, A2, B1 vs.
    description = models.TextField()

    def __str__(self):
        return self.name

class Lesson(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    audio_url = models.URLField(blank=True, null=True)
    transcript = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.conf import settings

class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    score = models.FloatField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'lesson']  # Aynı dersi birden fazla kez kayıtlamasın

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"
