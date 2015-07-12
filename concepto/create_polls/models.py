from django.db import models

# Create your models here.


class Poll(models.Model):
    question = models.CharField(max_length=200)
    question_text = models.TextField(max_length=2000)
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date published')
    created_by = models.IntegerField(default=0)
    stat_id = models.IntegerField(default=0)


class Answer(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.TextField(max_length=2000)
    vote_count = models.IntegerField(default=0)
    answer_img_url = models.IntegerField(default=0)
    answer_vid_url = models.IntegerField(default=0)
