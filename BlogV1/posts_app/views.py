from django.http import HttpResponse
from django.shortcuts import render
from models import Post, Category, Comment, Tag, Reply, Like, Dislike, Forbidden

# Create your views here.

def post(request, post_id):
    post = Post.objects.get(id = post_id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(comment_post__id = post_id)

    comments_replies = []

    for comment in comments:
        replies = Reply.objects.filter(reply_comment__id = comment.id)
        comments_replies.append(replies)

    context = {'post': post, 'categories': categories, 'comments':comments, 'replies':comments_replies}
    return render(request, 'post.html', context)

def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'home.html', context)

def category(request, cat_id):
    categories = Category.objects.all()
    category = Category.objects.get(id = cat_id)
    cat_posts = Post.objects.filter(post_category__id = cat_id)

    #cat_post = map(lambda x : x, cat_posts)

    context = {'category': category, 'categories': categories, 'cat_posts':cat_posts }

    return render(request, 'category.html', context)