from django.contrib import admin
from posts_app.models import Post ,  Tag

class PostModelAdmin(admin.ModelAdmin):
    list_display=["__unicode__","timestamp"]
    class Meta:
        model=Post

################################################

class InlineTag(admin.StackedInline):
    model = Tag
    extra = 3

