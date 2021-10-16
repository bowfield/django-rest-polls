from django.urls import path
from .views import PollView, AnswerView
from .views import MeView, AdminView
from .views import AdminPollsView, AdminNewPollView

urlpatterns = [
    # admin panel
    path('admin/', AdminView.as_view()),
    path('admin/polls/', AdminPollsView.as_view()),
    path('admin/polls/new/', AdminNewPollView.as_view()),

    # api
    path('polls/', PollView.as_view()),
    path('answer/', AnswerView.as_view()),
    path('me/', MeView.as_view()),
]
