from models import *
from Crypto.Hash import MD5
import time


def encrypt(data):
    data = data + str(time.time())
    return MD5.new(data).hexdigest()


def get_poll_data(poll_id):
    poll_dict = {}
    try:
        poll_obj = Polls.objects.get(id=poll_id)
        poll_dict = poll_obj.__dict__
        poll_dict.pop('_state')
        poll_dict['created_at'] = str(poll_dict['created_at'])
        poll_dict['updated_at'] = str(poll_dict['updated_at'])

        answers = Answers.objects.filter(poll=poll_obj)
        answers_dict = {}
        i = 0
        for option in answers:
            option_dict = option.__dict__
            option_dict.pop('_state')
            answers_dict[i] = option_dict
            i += 1
        poll_dict['options'] = answers_dict
    except Exception as e:
        print str(e)
    return poll_dict
