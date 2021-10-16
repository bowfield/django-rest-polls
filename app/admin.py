from django.contrib import admin
from .models import Poll, PollAnswer, User

admin.site.register(Poll)
admin.site.register(PollAnswer)
admin.site.register(User)