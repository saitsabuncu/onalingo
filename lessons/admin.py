from django.contrib import admin
from .models import Level, Lesson
from .models import UserProgress
from .models import SpeakingFeedback

admin.site.register(Level)
admin.site.register(Lesson)
admin.site.register(UserProgress)
admin.site.register(SpeakingFeedback)
