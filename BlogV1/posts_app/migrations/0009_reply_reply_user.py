# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_auto_20180214_1704'),
        ('posts_app', '0008_post_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='reply_user',
            field=models.ForeignKey(default=None, to='auth_app.User'),
        ),
    ]
