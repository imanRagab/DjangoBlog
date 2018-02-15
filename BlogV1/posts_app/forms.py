from django import forms
from models import Comment, Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'name': 'comment-text',
                'required': True,
                'placeholder': 'Make your words positive...',
                'class': "form-control"
            }),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply

        fields = ['reply_text']
        widgets = {
            'reply_text': forms.Textarea(attrs={
                'name': 'reply-text',
                'required': True,
                'placeholder': 'Make your words positive...',
                'class': "form-control",
            }),
        }