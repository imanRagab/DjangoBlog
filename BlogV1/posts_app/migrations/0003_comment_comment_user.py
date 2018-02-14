# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
        ('posts_app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_user',
            field=models.ForeignKey(default=None, to='auth_app.User'),
        ),
    ]
