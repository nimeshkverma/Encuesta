# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.TextField(max_length=2000)),
                ('vote_count', models.IntegerField(default=0)),
                ('answer_img_url', models.IntegerField(default=0)),
                ('answer_vid_url', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=200)),
                ('question_text', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(verbose_name=b'date published')),
                ('updated_at', models.DateTimeField(verbose_name=b'date published')),
                ('created_by', models.IntegerField(default=0)),
                ('stat_id', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='poll',
            field=models.ForeignKey(to='create_polls.Poll'),
            preserve_default=True,
        ),
    ]
