from django.shortcuts import render
from django.http import HttpResponse
from create_polls.models import Polls, Answers
import datetime


def make_poll(request):
    return render(request, '../templates/create_polls/make_poll.html')


def submit_poll(request):
    print request.POST
    question = request.POST["question"]
    description = request.POST["description"]
    choice_text = []
    for key in request.POST:
        print key
        if 'option' in key:
            choice_text.append(request.POST.get(key))
    poll_obj = Polls(question=question, description=description,
                     created_at=datetime.datetime.now(), updated_at=datetime.datetime.now())
    poll_obj.save()
    options_list = []
    for option in choice_text:
        ans_obj = Answers(poll=poll_obj, answer_text=option)
        options_list.append(ans_obj)
    Answers.objects.bulk_create(options_list)
    return render(request, '../templates/create_polls/submit_poll.html')
