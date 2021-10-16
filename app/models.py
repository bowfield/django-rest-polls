from django.db import models
from django.utils import timezone
import json

# опрос
class Poll(models.Model):
    text = models.CharField(max_length=30, default='')       # текст опроса
    type = models.CharField(max_length=10, default='')       # тип опроса
    start_date = models.DateTimeField(default=timezone.now)  # время старта
    end_date = models.DateTimeField(default=timezone.now)    # время окончания

    def __str__(self):
        return "id: {}, text: {}".format(self.id, self.text)

# ответ к опросу
class PollAnswer(models.Model):
    el = models.ForeignKey(related_name='answers', to=Poll, on_delete=models.CASCADE, null=True)
    poll = models.IntegerField()            # id опроса
    text = models.CharField(max_length=30)  # текст ответа

    def __str__(self):
        return "id: {}, text: {}".format(self.id, self.text)

# проголосвавший пользователь
class User(models.Model):
    el = models.ForeignKey(related_name='users', to=PollAnswer, on_delete=models.CASCADE, null=True)
    real_id = models.IntegerField()
    answer = models.IntegerField()
    value = models.CharField(default='', max_length=40, null=True, blank=True)

    def __str__(self):
        return 'id: {}'.format(self.id)