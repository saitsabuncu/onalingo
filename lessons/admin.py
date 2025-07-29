from django.contrib import admin
from .models import Level, Lesson
from .models import UserProgress

admin.site.register(Level)
admin.site.register(Lesson)
admin.site.register(UserProgress)
