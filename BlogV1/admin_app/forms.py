from django import forms
from posts_app.models import Post,Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        # fields = (
        #     'post_title',
        #     'post_content',
        #     'post_picture',
        #     'post_author',
        #     'post_created_at',
        #     'post_category_id',
        # )

################################################

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'category_name',
    )



