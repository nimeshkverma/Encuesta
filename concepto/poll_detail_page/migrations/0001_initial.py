# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('answer_text', models.TextField()),
                ('answer_img_url', models.CharField(max_length=255)),
                ('answer_vid_url', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category_Poll',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('category', models.ForeignKey(to='poll_detail_page.Categories')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mediums',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('question', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('stat', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField()),
                ('medium', models.ForeignKey(to='poll_detail_page.Mediums')),
                ('poll', models.ForeignKey(to='poll_detail_page.Polls')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('profession', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('ethinicity', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('loggedin', models.IntegerField()),
                ('answer', models.ForeignKey(to='poll_detail_page.Answers')),
                ('user', models.ForeignKey(to='poll_detail_page.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shares',
            name='user',
            field=models.ForeignKey(to='poll_detail_page.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='polls',
            name='user',
            field=models.ForeignKey(to='poll_detail_page.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category_poll',
            name='poll',
            field=models.ForeignKey(to='poll_detail_page.Polls'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answers',
            name='poll',
            field=models.ForeignKey(to='poll_detail_page.Polls'),
            preserve_default=True,
        ),
    ]
