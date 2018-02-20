# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0002_dislike_forbidden_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='dislike_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
