from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Question, Leaderboard, GameCompletionCounter

class QuestionAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        for i in range(6):
            Question.objects.create(
                question=f"Less Difficult Question {i+1}",
                difficulty='less',
                possible_answers=["Option A", "Option B", "Option C", "Option D"],
                correct_answer="Option A",
                url="http://example.com",
            )
        for i in range(6):
            Question.objects.create(
                question=f"More Difficult Question {i+1}",
                difficulty='more',
                possible_answers=["Option A", "Option B", "Option C", "Option D"],
                correct_answer="Option A",
                url="http://example.com",
            )

    def test_get_random_questions(self):
        response = self.client.get(reverse('questions'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 12)

        for question in response.data:
            self.assertIn('question', question)
            self.assertIn('difficulty', question)
            self.assertIn('possible_answers', question)
            self.assertIn('correct_answer', question)
            self.assertIn('url', question)
            self.assertEqual(len(question['possible_answers']), 4)

class LeaderboardAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Leaderboard.objects.create(name="Alice", points=100, time=30.0)
        Leaderboard.objects.create(name="Bob", points=150, time=25.0)

    def test_get_leaderboard(self):
        response = self.client.get(reverse('leaderboard'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        for entry in response.data:
            self.assertIn('name', entry)
            self.assertIn('points', entry)
            self.assertIn('time', entry)

    def test_post_leaderboard(self):
        data = {'name': 'Charlie', 'points': 120, 'time': 28.0}
        response = self.client.post(reverse('leaderboard'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Leaderboard.objects.count(), 3)

class GameCompletionCounterAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        GameCompletionCounter.objects.create(count=5)

    def test_post_game_completion(self):
        response = self.client.post(reverse('record-completion'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        counter = GameCompletionCounter.objects.get(id=1)
        self.assertEqual(counter.count, 6)