from rest_framework import serializers
from .models import Question, Choice, Scooter


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']


class ScooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scooter
        fields = 'all'