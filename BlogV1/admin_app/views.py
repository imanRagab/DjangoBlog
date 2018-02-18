from django.shortcuts import render
# from BlogV1.posts_app.forms import UserRegForm, ReplyForm, CommentForm

def dashboard(request):
    return render(request, 'admin/dashboard.html')





