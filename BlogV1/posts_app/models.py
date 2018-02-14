from django.db import models



class Category(models.Model):
    category_name = models.CharField(max_length=255)


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    post_content = models.TextField()
    post_category = models.ForeignKey(Category)
    post_picture = models.CharField(max_length=255)


class Comment(models.Model):
    comment_text = models.TextField()
    #comment_post = models.ForeignKey(User)

