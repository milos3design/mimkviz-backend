from django.urls import path
from .views import QuestionsAPIView, LeaderboardAPIView, GameCompletionCounterAPIView

urlpatterns = [
    path('questions/', QuestionsAPIView.as_view(), name='questions'),
    path('leaderboard/', LeaderboardAPIView.as_view(), name='leaderboard'),
    path('record-completion/', GameCompletionCounterAPIView.as_view(), name='record-completion'),
]