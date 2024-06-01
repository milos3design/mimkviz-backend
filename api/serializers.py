from rest_framework import serializers
from .models import Question, Leaderboard, GameCompletionCounter
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os

AES_KEY = os.getenv("AES_KEY")

FIXED_IV = os.getenv("IV_KEY").encode('utf-8')
print(FIXED_IV)
def encrypt_value(value: str) -> bytes:
    # Convert the input value to bytes and pad it
    padded_value = pad(value.encode('utf-8'), 16)
    cipher = AES.new(AES_KEY.encode('utf-8'), AES.MODE_CBC, iv=FIXED_IV)

    return base64.b64encode(cipher.encrypt(padded_value))

class QuestionSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['correct_answer'] = encrypt_value(instance.correct_answer)
        return data

    class Meta:
        model = Question
        fields = ['id', 'question', 'difficulty', 'possible_answers', 'correct_answer', 'url']


class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['id', 'name', 'points', 'time']


class GameCompletionCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCompletionCounter
        fields = ['count']