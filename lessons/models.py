from django.db import models

class Level(models.Model):
    name=models.CharField(max_length=10, unique=True) # A1, A2, B1 gibi
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    level=models.ForeignKey(Level, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    transcript = models.TextField()  # konuşma metni
    audio_url = models.URLField(blank=True, null=True)  # ses dosyası bağlantısı
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.level.name} - {self.title}"

