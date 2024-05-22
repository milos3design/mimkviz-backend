from django.shortcuts import render
from rest_framework import generics
from .models import Question, Leaderboard
from .serializers import QuestionSerializer, LeaderboardSerializer
import random

class QuestionsAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        less_difficult_questions = Question.objects.filter(difficulty='less')
        more_difficult_questions = Question.objects.filter(difficulty='more')

        less_difficult_selected = random.sample(list(less_difficult_questions), 6)
        more_difficult_selected = random.sample(list(more_difficult_questions), 6)

        # Shuffle possible answers for each question
        for question in less_difficult_selected + more_difficult_selected:
            random.shuffle(question.possible_answers)

        return less_difficult_selected + more_difficult_selected


class LeaderboardAPIView(generics.ListCreateAPIView):
    queryset = Leaderboard.objects.all()[:10]
    serializer_class = LeaderboardSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        name = data.get('name')
        points = data.get('points')
        time = data.get('time')

        # Check if the new score should be in the top 10
        leaderboard = Leaderboard.objects.all().order_by('-points', 'time')
        if leaderboard.count() < 10 or (leaderboard.last().points < points or (leaderboard.last().points == points and leaderboard.last().time > time)):
            if leaderboard.count() == 10:
                leaderboard.last().delete()
            Leaderboard.objects.create(name=name, points=points, time=time)

        return super().post(request, *args, **kwargs)