# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll_detail_page', '0002_auto_20150709_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
