from django.contrib import admin
from .models import Question

from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'difficulty', 'correct_answer']
    list_filter = ['difficulty']
    search_fields = ['question', 'correct_answer']
    fieldsets = [
        (None, {'fields': ['question', 'difficulty', 'url']}),
        ('Answers', {'fields': ['possible_answers', 'correct_answer']}),
    ]

admin.site.register(Question, QuestionAdmin)