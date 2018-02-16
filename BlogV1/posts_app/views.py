from django.shortcuts import render
from models import Post, Category, Comment, Tag, Reply, LikesDislikes
from django.contrib.auth.models import User
from .forms import  UserRegForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def post(request, post_id):
    post = Post.objects.get(id = post_id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(comment_post__id = post_id)
    reg_form = UserRegForm()

    comments_replies = []

    for comment in comments:
        replies = Reply.objects.filter(reply_comment__id = comment.id)
        comments_replies.append(replies)

    context = {'post': post, 'categories': categories, 'comments':comments, 'replies':comments_replies, 'reg_form':reg_form}
    return render(request, 'post.html', context)


def register_view(request):
    title="Register"
    form = UserRegForm(request.POST or None)
    if form.is_valid():
        user=form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

    context={
        "form":form,
        "title":title
     }
    return render(request, 'register.html', context)



def login_view(request):

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("logged in")
        else :
            return HttpResponse("you don`t exsit")

    return render(request , "login.html")

@login_required
def logged_in_only(request):
    return HttpResponse("you are authenticated")
