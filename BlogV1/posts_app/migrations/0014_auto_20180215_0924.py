# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0013_reply_reply_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='reply_created_at',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
