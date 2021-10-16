from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Poll, PollAnswer, User
from django.utils.safestring import SafeString
from datetime import datetime
from .serializers import PollSerializer, AnswerSerializer, UserSerializer
import json

# new API

# view для получения списка опросов
class PollView(APIView):
    def get(self, request):
        polls = Poll.objects.filter(start_date__lte=datetime.now(), end_date__gte=datetime.now())
        serializer = PollSerializer(polls, many=True)
        return Response({"polls": serializer.data})

# view для голосования
class AnswerView(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')

        answer_simple = request.data.get('answer_simple')
        answer_multiple = request.data.get('answer_multiple')
        answer_input = request.data.get('answer_input')

        if answer_simple != None: # single
            data = {
                "real_id": answer_simple['user_id'],
                "answer": answer_simple['answer_id']
            }
            serializer = UserSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                saved = serializer.save()

            answers = PollAnswer.objects.all()
            for answer in answers:
                if answer.id == data['answer']:
                    saved.el = answer
                    saved.save()

            return Response({"success": "Answer {} added".format(saved)})

        if answer_multiple != None: # multiple
            _answers = answer_multiple['answers']

            for _answer in _answers:
                data = {
                    "real_id": answer_multiple['user_id'],
                    "answer": _answer
                }
                serializer = UserSerializer(data=data)

                if serializer.is_valid(raise_exception=True):
                    saved = serializer.save()

                answers = PollAnswer.objects.all()
                for answer in answers:
                    if answer.id == _answer:
                        saved.el = answer
                        saved.save()

            return Response({"success": "Answers added"})

        if answer_input != None: # input
            data = {
                "real_id": answer_input['user_id'],
                "answer": -1,
                "value": answer_input['answer_input']
            }
            serializer = UserSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                saved = serializer.save()

            answers = PollAnswer.objects.all()
            for answer in answers:
                if answer.id == data['answer']:
                    saved.el = answer
                    saved.save()

            return Response({"success": "Answer {} added".format(saved)})

        return Response({"error": "Unknown usage"}, status=403)

# view для получения данных о себе
class MeView(APIView):
    def get(self, request):
        user_id = int(request.GET['user_id'])
        l = []

        for usr in User.objects.filter(real_id=user_id):
            answ = PollAnswer.objects.filter(id=usr.answer)[0]
            serializer = AnswerSerializer(answ)
            l.append(serializer.data)

        return Response({"data": l})

# ADMIN PANEL

# view для авторизации
class AdminView(APIView):
    def get(self, request):
        return render(request, "admin/auth.html", {})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        # fixme: hardcoded auth
        if username == "root" and password == "root":
            return redirect("/admin/polls/")

        return render(request, "admin/auth.html", {})

# view для просмотра и редактирования опросов
class AdminPollsView(APIView):
    def get(self, request):
        polls = []
        answers = []

        # getting polls
        for poll in Poll.objects.all():
            end = datetime.fromisoformat(str(poll.end_date)[:19][:10])
            now = datetime.now()
            to_end = end - now

            polls.append(
                {
                    "id": poll.id,
                    "text": poll.text,
                    "type": poll.type,
                    "start_date": str(poll.start_date)[:19][:10],
                    "end_date": str(poll.end_date)[:19][:10],
                    "to_end": to_end.days
                }
            )

        # getting answers
        for answer in PollAnswer.objects.all():
            answers.append(
                {
                    "poll": answer.poll,
                    "text": answer.text,
                    # "users": answer.users.replace('\"', '\'')
                }
            )

        data = {
            "polls": SafeString(json.dumps(polls).replace("\"", "\\\"")),
            "answers": SafeString(json.dumps(answers).replace("\"", "\\\""))
        }

        return render(request, "admin/polls.html", data)

    def post(self, request):
        id = request.POST['id']
        text = request.POST['text']
        end_date = request.POST['end_date']
        answers = [request.POST['answer1'], request.POST['answer2'], request.POST['answer3']]

        poll = Poll.objects.filter(id=id)[0]
        poll.text = text
        poll.end_date = datetime.fromisoformat(str(end_date)[:19])
        poll.save()

        if answers[0] != "":
            i = 0
            for answer in PollAnswer.objects.filter(poll=id):
                answer.text = answers[i]
                answer.save()
                i += 1

        return redirect("/admin/polls/")

# view создания новых опросов
class AdminNewPollView(APIView):
    def get(self, request):
        return render(request, 'admin/new_poll.html', {})

    def post(self, request):
        text = request.POST["text"]
        _type = request.POST["type"]
        date_start = request.POST["date_start"]
        date_end = request.POST["date_end"]
        answer1 = request.POST["answer1"]
        answer2 = request.POST["answer2"]
        answer3 = request.POST["answer3"]

        # создаем опрос
        poll = Poll.objects.create(text=text, type=_type, start_date=date_start, end_date=date_end)
        poll.save()

        # создаем ответ 1
        answ1 = PollAnswer.objects.create(poll=poll.id, text=answer1)
        answ1.el = poll # линкуем опрос
        answ1.save()
        if _type != "input": # если не ответ в виде строки
            # добавляем еще ответ
            answ2 =PollAnswer.objects.create(poll=poll.id, text=answer2)
            answ2.el = poll # линкуем опрос
            answ2.save()

            # добавляем еще ответ
            answ3 = PollAnswer.objects.create(poll=poll.id, text=answer3)
            answ3.el = poll # линкуем опрос
            answ3.save()

        return redirect("/admin/polls/")