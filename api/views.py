from django.shortcuts import render
from rest_framework import generics
from .models import Question
from .serializers import QuestionSerializer
import random

class QuestionsAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        less_difficult_questions = Question.objects.filter(difficulty='less')
        more_difficult_questions = Question.objects.filter(difficulty='more')

        less_difficult_selected = random.sample(list(less_difficult_questions), 5)
        more_difficult_selected = random.sample(list(more_difficult_questions), 5)

        # Shuffle possible answers for each question
        for question in less_difficult_selected + more_difficult_selected:
            random.shuffle(question.possible_answers)

        return less_difficult_selected + more_difficult_selected
