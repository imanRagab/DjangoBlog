from django.contrib import admin

from posts_app.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display=["__unicode__","timestamp"]
    class Meta:
        model=Post