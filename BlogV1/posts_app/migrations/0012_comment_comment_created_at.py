# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0011_auto_20180215_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
