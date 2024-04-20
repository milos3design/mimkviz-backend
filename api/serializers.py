from rest_framework import serializers
from .models import Question
from cryptography.fernet import Fernet
import os

cipher_suite = Fernet(os.getenv("FERNET_KEY"))

class QuestionSerializer(serializers.ModelSerializer):
    correct_answer = serializers.SerializerMethodField()

    def get_correct_answer(self, obj):
        if obj.correct_answer:
            # Encrypt correct answer
            return cipher_suite.encrypt(obj.correct_answer.encode()).decode()
        return None
    
    class Meta:
        model = Question
        fields = ['id', 'question', 'difficulty', 'possible_answers', 'correct_answer', 'url']