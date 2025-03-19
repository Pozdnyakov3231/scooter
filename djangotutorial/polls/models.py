import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text 
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class Scooter(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступен'),
        ('rented', 'Арендован'),
        ('maintenance', 'На обслуживании'),
    ]

    model = models.CharField(max_length=100)
    battery_capacity = models.IntegerField(default=100)  # Новое поле: емкость аккумулятора (в %)
    battery_level = models.IntegerField(default=100)  # Текущий заряд
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    last_maintenance_date = models.DateTimeField(default=timezone.now)

    def str(self):
        return f"{self.model} - {self.battery_level}% / {self.battery_capacity}%"