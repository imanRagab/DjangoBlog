# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0010_auto_20180215_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
