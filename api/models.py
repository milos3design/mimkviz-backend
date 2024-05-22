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
    name = models.CharField(max_length=255)
    points = models.IntegerField()
    time = models.FloatField()

    class Meta:
        ordering = ['-points', 'time']  # Order by points descending, then by time ascending

    def __str__(self):
        return f'{self.name} - {self.points} points in {self.time} seconds'