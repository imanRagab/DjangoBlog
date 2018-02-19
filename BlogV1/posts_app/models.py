from django.db import models
from django.utils import timezone
from django.apps import apps
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_category = models.ForeignKey(Category)
    post_picture = models.CharField(max_length=255)
    post_author = models.CharField(max_length=255, default=None)
    post_created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.post_title


class Comment(models.Model):
    comment_text = models.TextField()
    comment_user = models.ForeignKey(User, blank=True)
    comment_post = models.ForeignKey(Post)
    comment_created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment_user.username \
               + " has commented "\
               + self.comment_text \
               + " on " \
               + self.comment_post.post_title


class Reply(models.Model):
    reply_text = models.TextField()
    reply_comment = models.ForeignKey(Comment)
    reply_user = models.ForeignKey(User, default=None)
    reply_created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reply_user.username \
               + " has replied " \
               + self.reply_text \
               + " to " \
               + self.reply_comment.comment_user.username \
               + "'s comment on " \
               + self.reply_comment.comment_post.post_title


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    tag_posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.tag_name


class Like(models.Model):
    like_user = models.ForeignKey(User)
    like_post = models.ForeignKey(Post)

    def __str__(self):
        return self.like_user.username + " likes " + self.like_post.post_title


class Dislike(models.Model):
    dislike_user = models.ForeignKey(User)
    dislike_post = models.ForeignKey(Post)

    def __str__(self):
        return self.dislike_user.username + " dislikes " + self.dislike_post.post_title


class CategorySubscribtion(models.Model):
    subscribed_category = models.ForeignKey(Category)
    subscribed_user = models.ForeignKey(User, default=None)

    def __str__(self):
        return self.subscribed_user.username + " has subscribed to " + self.subscribed_category.category_name

class Forbidden(models.Model):
    word = models.CharField(max_length=255)

    def __str__(self):
        return self.word
