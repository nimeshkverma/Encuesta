# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll_detail_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer_img_url',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answers',
            name='answer_vid_url',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='polls',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='polls',
            name='stat',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='polls',
            name='user',
            field=models.ForeignKey(to='poll_detail_page.Users', null=True),
            preserve_default=True,
        ),
    ]
