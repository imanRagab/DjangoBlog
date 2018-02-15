# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0004_reply_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='posts',
            new_name='tag_post',
        ),
    ]
