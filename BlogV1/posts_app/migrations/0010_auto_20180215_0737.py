# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0009_reply_reply_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_created_at',
            field=models.DateTimeField(default=datetime.date(2015, 1, 1)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(to='auth_app.User', blank=True),
        ),
    ]
