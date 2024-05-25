from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.utils import timezone
from .models import Question, Leaderboard
from .serializers import QuestionSerializer, LeaderboardSerializer
import random
from rest_framework.permissions import BasePermission
from django.http import HttpResponseForbidden

class IsLocalhost5173(BasePermission):
    def has_permission(self, request, view):
        # Check if the request is coming from localhost:5173
        return request.get_host() == 'http://localhost:5173'


class RestrictedAPIViewMixin:
    permission_classes = [IsLocalhost5173]


class QuestionsAPIView(RestrictedAPIViewMixin, generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        less_difficult_questions = Question.objects.filter(difficulty='less')
        more_difficult_questions = Question.objects.filter(difficulty='more')

        less_difficult_selected = random.sample(list(less_difficult_questions), 4)
        more_difficult_selected = random.sample(list(more_difficult_questions), 2)

        # Shuffle possible answers for each question
        for question in less_difficult_selected + more_difficult_selected:
            random.shuffle(question.possible_answers)

        return less_difficult_selected + more_difficult_selected

class LeaderboardAPIView(RestrictedAPIViewMixin, generics.ListCreateAPIView):
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
        else:
            return HttpResponseForbidden("You are not allowed to perform this action.")