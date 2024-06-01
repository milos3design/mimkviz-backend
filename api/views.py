from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.utils import timezone
from django.db.models import F
from .models import Question, Leaderboard, GameCompletionCounter
from .serializers import QuestionSerializer, LeaderboardSerializer, GameCompletionCounterSerializer
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
    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        return Leaderboard.objects.order_by('-points', 'time', '-created_at')[:10]

    def post(self, request, *args, **kwargs):
        data = request.data
        name = data.get('name')
        points = data.get('points')
        time = data.get('time')

        leaderboard = list(self.get_queryset())

        if len(leaderboard) < 10 or (points, time, timezone.now()) > (leaderboard[-1].points, leaderboard[-1].time, leaderboard[-1].created_at):
            # Create the new entry
            new_entry = Leaderboard.objects.create(name=name, points=points, time=time)

            # Return the updated leaderboard
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class GameCompletionCounterAPIView(generics.GenericAPIView):
    queryset = GameCompletionCounter.objects.all()
    serializer_class = GameCompletionCounterSerializer

    def post(self, request, *args, **kwargs):
        counter, _ = GameCompletionCounter.objects.get_or_create(id=1)
        counter.count = F('count') + 1
        counter.save(update_fields=['count'])
        counter.refresh_from_db()
        return Response({'count': counter.count})