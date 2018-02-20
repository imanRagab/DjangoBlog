from django import forms
from posts_app.models import Post, Category, Tag, Forbidden


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

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()

################################################

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'category_name',
    )


################################################

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = (
            'tag_name',
        )

################################################


class ForbiddenForm(forms.ModelForm):
    class Meta:
        model = Forbidden
        fields = (
            'word',
        )
