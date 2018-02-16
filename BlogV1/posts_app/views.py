from django.http import HttpResponse
from django.shortcuts import render
from models import Post, Category, Comment, Tag, Reply, Like, Dislike, Forbidden
from forms import ReplyForm, CommentForm

# Create your views here.

def post(request, post_id):
    comment_form = CommentForm()
    reply_form = ReplyForm()
    post = Post.objects.get(id = post_id)
    tags = Tag.objects.filter(tag_posts__id = post_id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(comment_post__id = post_id)

    comments_replies = []

    for comment in comments:
        replies = Reply.objects.filter(reply_comment__id = comment.id)
        comments_replies.append(replies)

    context = {'post': post, 'categories': categories,
               'comments':comments, 'replies':comments_replies,
               'comment_form':comment_form,
               'reply_form':reply_form,
               'tags':tags}

    return render(request, 'post.html', context)

def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'home.html', context)

def category(request, cat_id):
    categories = Category.objects.all()
    category = Category.objects.get(id = cat_id)
    context = {'category': category , 'categories': categories}
    cat_posts = Post.objects.filter(post_category__id=cat_id)

    # cat_post = map(lambda x : x, cat_posts)

    context = {'category': category, 'categories': categories, 'cat_posts': cat_posts}

    return render(request, 'category.html', context)


def comment_reply(request):
    if request.method == 'GET':
        comment_id = request.GET['comment_id']
        comment = Comment.objects.get(pk=comment_id)
        text = request.GET['reply_text']
        print text
        reply = Reply(reply_comment=comment, reply_text=text, reply_user=request.user)
        reply.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")

