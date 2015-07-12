# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll_detail_page', '0003_auto_20150709_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votes',
            name='user',
            field=models.ForeignKey(to='poll_detail_page.Users', null=True),
            preserve_default=True,
        ),
    ]
