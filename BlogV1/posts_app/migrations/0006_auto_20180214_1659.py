# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
        ('posts_app', '0005_auto_20180214_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorySubscribtion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscribed_category', models.ForeignKey(to='posts_app.Category')),
                ('subscribed_user', models.ForeignKey(default=None, to='auth_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='LikesDislikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField()),
                ('likes_dislikes_post', models.ForeignKey(to='posts_app.Post')),
                ('likes_dislikes_user', models.ForeignKey(default=None, to='auth_app.User')),
            ],
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag_post',
            new_name='tag_posts',
        ),
    ]
