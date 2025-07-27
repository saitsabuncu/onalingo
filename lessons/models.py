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
