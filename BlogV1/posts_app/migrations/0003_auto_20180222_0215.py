# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0002_poststags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_posts',
        ),
        migrations.AddField(
            model_name='post',
            name='post_tags',
            field=models.ManyToManyField(to='posts_app.Tag'),
        ),
    ]
