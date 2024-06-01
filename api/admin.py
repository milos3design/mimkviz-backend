from django.contrib import admin
from .models import Question, Leaderboard, GameCompletionCounter

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
    list_display = ['id', 'name', 'points', 'time', 'created_at']
    search_fields = ['name']
    ordering = ('-points', 'time', '-created_at')

admin.site.register(Leaderboard, LeaderboardAdmin)


class GameCompletionCounterAdmin(admin.ModelAdmin):
    list_display = ['id', 'count']

admin.site.register(GameCompletionCounter, GameCompletionCounterAdmin)