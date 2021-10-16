from django.db.models import Prefetch
from rest_framework import serializers
from .models import Poll, PollAnswer, User
from django.utils import timezone

class UserSerializer(serializers.Serializer):
    real_id = serializers.IntegerField()
    answer = serializers.IntegerField() #CreateOnlyDefault(default=-1)
    value = serializers.CharField(max_length=40, default=None)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class AnswerSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    poll = serializers.IntegerField()
    text = serializers.CharField(max_length=30)
    # users = serializers.CharField(max_length=9999)
    users = UserSerializer(many=True)

class PollSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    text = serializers.CharField(default='')
    type = serializers.CharField(max_length=10, default='')
    start_date = serializers.DateTimeField(default=timezone.now)
    end_date = serializers.DateTimeField(default=timezone.now)
    answers = AnswerSerializer(many=True)

    # def create(self, validated_data):
    #     return Poll.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.text = validated_data.get('text', instance.text)
    #     instance.end_date = validated_data.get('end_date', instance.end_date)
    #     instance.save()
    #     return instance