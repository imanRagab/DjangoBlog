from django import forms
from posts_app.models import Post, Category, Tag, Forbidden


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    class Meta:
        model = Post
        # fields = "__all__"
        fields = [
            'post_title',
            'post_author',
            'post_category',
            'post_content',
            'post_picture',
            'tags'

        ]

        def __init__(self, *args, **kwargs):
            if kwargs.get('instance'):
                initial = kwargs.setdefault('initial', {})
                initial['tags'] = [t.pk for t in kwargs['instance'].tag_set.all()]

            forms.ModelForm.__init__(self, *args, **kwargs)

        def save(self):
            instance = forms.ModelForm.save(self)
            instance.tag_set.clear()
            for tag in self.cleaned_data['tags']:
                instance.tag_set.add(tag)


################################################
#
# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.ImageField()

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
