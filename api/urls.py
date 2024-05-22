from django.urls import path
from .views import QuestionsAPIView, LeaderboardAPIView

urlpatterns = [
    path('questions/', QuestionsAPIView.as_view(), name='questions'),
    path('leaderboard/', LeaderboardAPIView.as_view(), name='leaderboard'),
]