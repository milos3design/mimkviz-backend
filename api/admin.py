from django.contrib import admin
from .models import Question, Leaderboard

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'difficulty', 'correct_answer']
    list_filter = ['difficulty']
    search_fields = ['question', 'correct_answer']
    fieldsets = [
        (None, {'fields': ['question', 'difficulty', 'url']}),
        ('Answers', {'fields': ['possible_answers', 'correct_answer']}),
    ]

admin.site.register(Question, QuestionAdmin)


class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['name', 'points', 'time']
    search_fields = ['name']
    list_filter = ['points']
    ordering = ['-points', 'time']

admin.site.register(Leaderboard, LeaderboardAdmin)