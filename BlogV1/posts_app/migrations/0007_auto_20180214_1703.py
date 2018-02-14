# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_app', '0006_auto_20180214_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likesdislikes',
            name='type',
            field=models.IntegerField(choices=[(1, b'like'), (0, b'dislike')]),
        ),
    ]
