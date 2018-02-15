# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0012_comment_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='reply_created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
