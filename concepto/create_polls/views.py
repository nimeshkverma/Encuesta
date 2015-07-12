from django.shortcuts import render
from django.http import HttpResponse
from create_polls.models import Poll, Answer
import datetime


def make_poll(request):
    return render(request, '../templates/create_polls/make_poll.html')


def submit_poll(request):
    question = request.POST["question"]
    question_text = request.POST["question_text"]
    choice_text = []
    for i in xrange(1, 5):
        choice_text.append(request.POST["option" + str(i)])
    que = Poll(question=question, question_text=question_text,
               created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
    que.save()
    print choice_text
    for i in xrange(1, 5):
        ans = Answer(poll=que, choice_text=choice_text[i - 1])
        ans.save()
    return render(request, '../templates/create_polls/submit_poll.html')
