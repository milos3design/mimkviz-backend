from django.db import models

class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('less', 'Less Difficult'),
        ('more', 'More Difficult'),
    ]
    question = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    possible_answers = models.JSONField()
    correct_answer = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.question
    

class Leaderboard(models.Model):
    name = models.CharField(max_length=16)
    points = models.IntegerField()
    time = models.DecimalField(max_digits=4, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)  # New field

    def __str__(self):
        return f"{self.name} - {self.points} points - {self.time} seconds - Created at: {self.created_at}"
    

class GameCompletionCounter(models.Model):
    count = models.IntegerField(default=0)