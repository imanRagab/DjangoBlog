# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0014_auto_20180215_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='reply_created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
