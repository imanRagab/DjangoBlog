from django.http import HttpResponse
from django.shortcuts import render
from models import Post, Category, Comment, Tag, Reply
from django.contrib.auth.models import User
from .forms import UserRegForm
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from models import Post, Category, Comment, Tag, Reply, Like, Dislike, Forbidden
from forms import ReplyForm, CommentForm


##########################################

def post(request, post_id):
    comment_form = CommentForm()
    reply_form = ReplyForm()
    post = Post.objects.get(id=post_id)
    tags = Tag.objects.filter(tag_posts__id=post_id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(comment_post__id=post_id)
    reg_form = UserRegForm()
    comments_replies = []

    for comment in comments:
        replies = Reply.objects.filter(reply_comment__id=comment.id)
        comments_replies.append(replies)
    context = {'post': post, 'categories': categories,
               'comments': comments, 'replies': comments_replies,
               'comment_form': comment_form,
               'reply_form': reply_form,
               'tags': tags, }

    return render(request, 'post.html', context)


###########################################

def register_view(request):
    title = "Register"
    form = UserRegForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

    context = {
        "form": form,
        "title": title
    }
    return render(request, 'register.html', context)


############################################

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home.html')
            else:
                return HttpResponse("Your account has been blocked please contact the admin")

        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


#################################################

@login_required
def logged_in_only(request):
    return HttpResponse("you are authenticated")
    context = {'post': post, 'categories': categories,
               'comments': comments, 'replies': comments_replies,
               'comment_form': comment_form,
               'reply_form': reply_form,
               'tags': tags}

    return render(request, 'post.html', context)


#################################################

def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'home.html', context)


################################################

def category(request, cat_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=cat_id)

    # return HttpResponse(category)
    cat_posts = Post.objects.filter(post_category__id=cat_id)

    # cat_post = map(lambda x : x, cat_posts)

    context = {'category': category, 'categories': categories, 'cat_posts': cat_posts}

    return render(request, 'category.html', context)


#################################################

def comment_reply(request, post_id, comment_id):
    if request.method == 'GET':
        reply_text = request.GET['reply_text']

        forbidden_words = Forbidden.objects.all()

        for forbidden_word in forbidden_words:
            reply_text = reply_text.replace(forbidden_word.word, ("*" * len(forbidden_word.word)))

        comment = Comment.objects.get(pk=comment_id)
        reply = Reply(reply_comment=comment, reply_text=reply_text, reply_user=request.user)
        reply.save()
        return HttpResponseRedirect('/ourblog/post/' + post_id)

    else:
        return HttpResponse("Request method is not a GET")


#################################################


def post_comment(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(pk=post_id)
        comment_text = request.GET['comment_text']
        forbidden_words = Forbidden.objects.all()

        for forbidden_word in forbidden_words:
            comment_text = comment_text.replace(forbidden_word.word, ("*" * len(forbidden_word.word)))

        comment = Comment(comment_post=post, comment_text=comment_text, comment_user=request.user)
        comment.save()

        return HttpResponseRedirect('/ourblog/post/' + post_id)

    else:
        return HttpResponse("Request method is not a GET")


#################################################

def like_post(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Post.objects.get(pk=post_id)
        like = Like(like_post=post, like_user=request.user)
        like.save()

        return HttpResponseRedirect('/ourblog/post/' + post_id)

    else:
        return HttpResponse("Request method is not a GET")

######################################################
def logout_view(request):
	logout(request)
	return render(request,'home.html')
