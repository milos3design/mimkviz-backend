from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Question

class QuestionAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_random_questions(self):
        # Create some sample questions
        for i in range(4):
            Question.objects.create(
                question=f"Question {i+1}",
                difficulty='less' if i < 2 else 'more',
                possible_answers=["Option A", "Option B", "Option C", "Option D"],
                correct_answer="Option A",
                url="example",
            )

        # Get random questions
        response = self.client.get(reverse('questions'))

        # Assert response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that 4 questions are returned
        self.assertEqual(len(response.data), 4)

        # Assert that each question has the required fields
        for question in response.data:
            self.assertIn('question', question)
            self.assertIn('difficulty', question)
            self.assertIn('possible_answers', question)
            self.assertIn('correct_answer', question)
            self.assertIn('url', question)
            self.assertEqual(len(question['possible_answers']), 4)