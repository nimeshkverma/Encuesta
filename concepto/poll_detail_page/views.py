from django.shortcuts import render
from utils import *
import json
from models import *
from django.http import HttpResponse
import datetime
# Create your views here.


def view_poll(request):
    poll_id = request.GET['id']
    http_response = HttpResponse()
    poll_details = get_poll_data(poll_id)
    http_response = render(
        request, '../templates/poll_detail_page/poll_answer.html', {"poll_data": json.dumps(poll_details)})
    if not request.COOKIES.get('uid'):
        value = encrypt(
            str(request.COOKIES.get('csrftoken')) + str(request.META.get('HTTP_USER_AGENT')))
        http_response.set_cookie(key='uid', value=value)
    return http_response


def record_user_choice(request):
    uid = request.COOKIES.get('uid') or ''
    option_choice = int(request.POST.get('poll_choice'))
    answer_obj = Answers.objects.get(id=option_choice)
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()
    logged_in = 0
    vote_obj = Votes(answer=answer_obj, created_at=created_at,
                     updated_at=updated_at, loggedin=logged_in)
    vote_obj.save()

    poll_votes = Votes.objects.filter(answer__poll__id=answer_obj.poll_id)
    available_choices = Answers.objects.filter(poll__id=answer_obj.poll_id)
    vote_stats = {}
    for option in available_choices:
        if 'options' not in vote_stats:
            vote_stats['options'] = {}
        if option.answer_text not in vote_stats['options']:
            vote_stats['options'][option.answer_text] = 0
        for vote in poll_votes:
            if vote.answer_id == option.id:
                vote_stats['options'][option.answer_text] += 1
    vote_stats['question'] = answer_obj.poll.question
    return render(request, '../templates/poll_detail_page/stats_visualize.html', {"vote_count": json.dumps(vote_stats)})
