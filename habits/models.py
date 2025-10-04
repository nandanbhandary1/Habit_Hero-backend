from django.db import models


class Habit(models.Model):
    name = models.CharField(max_length=255)
    frequency = models.CharField(max_length=10)  # daily, weekly
    category = models.CharField(max_length=50)
    start_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class CheckIn(models.Model):  # Make sure "I" is capital
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
