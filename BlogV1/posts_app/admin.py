from django.contrib import admin
from .models import Category, Post, Comment, Reply, Tag, Like, Dislike, CategorySubscribtion, Forbidden


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Forbidden)
admin.site.register(CategorySubscribtion)


