# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0007_auto_20180214_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_author',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
