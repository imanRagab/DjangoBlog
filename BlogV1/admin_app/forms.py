from django import forms
from posts_app.models import Post, Category
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = (_all_)
        fields = (
            'post_title',
            'post_content',
            'post_picture',
            'post_author',
            # 'post_created_at',
            # 'post_category_id',
        )

################################################

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'category_name',
    )




class userForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    cpassword = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'cpassword'
        ]