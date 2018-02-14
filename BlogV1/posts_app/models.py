from django.db import models
from django.apps import apps
#User = apps.get_model('auth_app', 'User')

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

    def __str__(self):
        return self.post_title



class Comment(models.Model):
    comment_text = models.TextField()
    comment_user = models.ForeignKey('auth_app.User', default=None)
    comment_post = models.ForeignKey(Post)

    def __str__(self):
        return self.comment_text


class Reply(models.Model):
    reply_text = models.TextField()
    reply_comment = models.ForeignKey(Comment)
    reply_user = models.ForeignKey('auth_app.User', default=None)

    def __str__(self):
        return self.reply_text


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    tag_posts = models.ManyToManyField(Post)

    def __str__(self):
        return self.tag_name


class LikesDislikes(models.Model):
    likes_dislikes_user = models.ForeignKey('auth_app.User', default=None)
    likes_dislikes_post = models.ForeignKey(Post)
    type = models.IntegerField(choices=((1, 'like'), (0, 'dislike'))) #1 for like 0 for dislike

    def __str__(self):
        if self.type == 1:
            return self.likes_dislikes_user.username + " likes " + self.likes_dislikes_post.post_title
        else:
            return self.likes_dislikes_user.username + " dislikes " + self.likes_dislikes_post.post_title

class CategorySubscribtion(models.Model):
    subscribed_category = models.ForeignKey(Category)
    subscribed_user = models.ForeignKey('auth_app.User', default=None)

    def __str__(self):
        return self.subscribed_user.username + " has subscribed to " + self.subscribed_category.category_name